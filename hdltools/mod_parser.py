#
# Copyright (C) 2025-2026 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
Parses SystemVerilog modules to extract information about parameters
and ports using a robust AST-based approach (pyslang).
"""

from pyslang.driver import Driver


class ModParser:
    """Extract params, localparams, and ports from SV modules."""

    def __init__(self, file_path='', defines=None):
        """Initializes the parser with a target file and macros."""
        self.modules = {}
        self.file_path = file_path
        self.defines = defines if defines else []

    def set_file(self, file_path):
        """Sets the SystemVerilog HDL file path."""
        self.file_path = file_path

    def set_defines(self, defines):
        """Sets the macro definitions for the preprocessor."""
        self.defines = defines

    def _clean_token(self, token):
        """Robustly extracts clean string value from a pyslang Token."""
        if not token:
            return ""

        if hasattr(token, "valueText") and token.valueText:
            return str(token.valueText)

        if hasattr(token, "value") and token.value:
            val = str(token.value).strip()
            if val:
                return val

        parts = str(token).split()
        return parts[-1] if parts else ""

    def _extract_dimensions(self, dimensions):
        """Joins dimensions safely without whitespace or trivia."""
        if not dimensions:
            return ""

        dim_str = ""
        for d in dimensions:
            clean_d = str(d).replace(" ", "").replace("\n", "")
            clean_d = clean_d.replace("\r", "").replace("\t", "")
            dim_str += clean_d

        return dim_str

    def _extract_type_info(self, type_node):
        """Extracts base type, signing, and packed dimensions."""
        result = {}
        if not type_node:
            return result

        kw = ""
        if hasattr(type_node, "keyword") and type_node.keyword:
            kw = self._clean_token(type_node.keyword)
        elif hasattr(type_node, "name") and type_node.name:
            kw = self._clean_token(type_node.name)

        if kw:
            result["type"] = kw

        if hasattr(type_node, "signing") and type_node.signing:
            sign_str = self._clean_token(type_node.signing)
            if sign_str:
                result["sign"] = sign_str

        if hasattr(type_node, "dimensions") and type_node.dimensions:
            packed_str = self._extract_dimensions(type_node.dimensions)
            if packed_str:
                result["packed"] = packed_str

        return result

    def _extract_header_attrs(self, header):
        """Extracts direction, netType, varKeyword, and dataType."""
        attrs = {}
        if not header:
            return attrs

        dir_val = self._clean_token(getattr(header, "direction", None))
        net_val = self._clean_token(getattr(header, "netType", None))
        var_val = self._clean_token(getattr(header, "varKeyword", None))

        type_node = getattr(
            header, "dataType", getattr(header, "type", None)
        )
        type_info = self._extract_type_info(type_node) if type_node else {}

        if dir_val or net_val or var_val or type_info:
            if dir_val:
                attrs["direction"] = dir_val

            combined = []
            if net_val:
                combined.append(net_val)
            if var_val:
                combined.append(var_val)

            dt_str = type_info.pop("type", "")
            if dt_str:
                combined.append(dt_str)

            if combined:
                attrs["type"] = " ".join(combined)

            attrs.update(type_info)

        return attrs

    def _extract_body_decl_attrs(self, node):
        """Extracts type attributes from declarations in the body."""
        attrs = {}
        combined = []

        net_val = self._clean_token(getattr(node, "netType", None))
        if net_val:
            combined.append(net_val)

        if hasattr(node, "modifiers") and node.modifiers:
            for mod in node.modifiers:
                mod_str = self._clean_token(mod)
                if mod_str == "var":
                    combined.append("var")

        type_node = getattr(node, "dataType", getattr(node, "type", None))
        type_info = self._extract_type_info(type_node) if type_node else {}

        dt_str = type_info.pop("type", "")
        if dt_str:
            combined.append(dt_str)

        if combined:
            attrs["type"] = " ".join(combined)

        attrs.update(type_info)
        return attrs

    def _apply_declarator_attrs(self, decl, target_dict):
        """Extracts unpacked dimensions and initializer from a declarator."""
        if hasattr(decl, "dimensions") and decl.dimensions:
            unpacked = self._extract_dimensions(decl.dimensions)
            if unpacked:
                target_dict["unpacked"] = unpacked

        if hasattr(decl, "initializer") and decl.initializer:
            init_str = str(decl.initializer)
            init_str = init_str.replace("=", "", 1).strip()
            if init_str:
                target_dict["default"] = init_str

    def _process_parameter_list(self, param_decl, mod_dict):
        """Processes a ParameterDeclaration node."""
        if not param_decl:
            return

        keyword = self._clean_token(getattr(param_decl, "keyword", None))
        if keyword == "localparam":
            target_group = "localparams"
        else:
            target_group = "parameters"

        target_dict = mod_dict[target_group]
        type_node = getattr(
            param_decl, "type", getattr(param_decl, "dataType", None)
        )
        type_info = self._extract_type_info(type_node)

        if not hasattr(param_decl, "declarators"):
            return

        for decl in param_decl.declarators:
            if str(decl).strip() == ",":
                continue
            if not hasattr(decl, "name"):
                continue

            param_name = self._clean_token(decl.name)
            if not param_name:
                continue

            param_dict = {}
            param_dict.update(type_info)
            self._apply_declarator_attrs(decl, param_dict)
            target_dict[param_name] = param_dict

    def _handle_non_ansi_port(self, port, mod_dict):
        """Registers a Non-ANSI port name in the dictionary."""
        if hasattr(port, "expr") and hasattr(port.expr, "name"):
            port_name = self._clean_token(port.expr.name)
            if port_name:
                mod_dict["ports"][port_name] = {}

    def _handle_ansi_port(self, port, mod_dict, curr_h_attrs):
        """Processes an ANSI port and returns current header attrs."""
        port_dict = {}
        if hasattr(port, "header") and port.header:
            h_attrs = self._extract_header_attrs(port.header)
            if h_attrs:
                curr_h_attrs = h_attrs

        port_dict.update(curr_h_attrs)

        if hasattr(port, "declarator") and port.declarator:
            decl = port.declarator
            p_name = self._clean_token(decl.name)
            if p_name:
                self._apply_declarator_attrs(decl, port_dict)
                mod_dict["ports"][p_name] = port_dict

        return curr_h_attrs

    def _process_header_ports(self, port_list, mod_dict):
        """Extracts port declarations from the module header."""
        is_non_ansi = "NonAnsi" in port_list.kind.name
        curr_h_attrs = {}

        for port in port_list.ports:
            if str(port).strip() == ",":
                continue

            if is_non_ansi:
                self._handle_non_ansi_port(port, mod_dict)
            else:
                curr_h_attrs = self._handle_ansi_port(
                    port, mod_dict, curr_h_attrs
                )

    def _process_body_port_decl(self, body_member, mod_dict):
        """Processes a PortDeclaration in the module body."""
        h_node = getattr(body_member, "header", None)
        h_attrs = self._extract_header_attrs(h_node)

        if not hasattr(body_member, "declarators"):
            return

        for decl in body_member.declarators:
            if str(decl).strip() == ",":
                continue
            if not hasattr(decl, "name"):
                continue

            p_name = self._clean_token(decl.name)
            p_dict = mod_dict["ports"]
            if p_name and p_name in p_dict:
                port_data = p_dict[p_name]
                port_data.update(h_attrs)
                self._apply_declarator_attrs(decl, port_data)

    def _process_body_data_decl(self, body_member, mod_dict):
        """Processes a DataDeclaration or NetDeclaration in the body."""
        decl_attrs = self._extract_body_decl_attrs(body_member)

        if not hasattr(body_member, "declarators"):
            return

        for decl in body_member.declarators:
            if str(decl).strip() == ",":
                continue
            if not hasattr(decl, "name"):
                continue

            p_name = self._clean_token(decl.name)
            p_dict = mod_dict["ports"]
            if p_name and p_name in p_dict:
                port_data = p_dict[p_name]
                port_data.update(decl_attrs)
                self._apply_declarator_attrs(decl, port_data)

    def _process_body_members(self, members, mod_dict):
        """Iterates and parses logic and declarations inside the module."""
        for body_member in members:
            kind_name = body_member.kind.name

            if "ParameterDeclarationStatement" in kind_name:
                param_decl = getattr(body_member, "parameter", None)
                if param_decl:
                    self._process_parameter_list(param_decl, mod_dict)

            elif "PortDeclaration" in kind_name:
                self._process_body_port_decl(body_member, mod_dict)

            elif ("DataDeclaration" in kind_name or
                  "NetDeclaration" in kind_name):
                self._process_body_data_decl(body_member, mod_dict)

    def _run_slang(self):
        """Configures and runs the pyslang compiler driver."""
        driver = Driver()
        driver.addStandardArgs()

        args = ["slang"]
        for macro in self.defines:
            args.append(f"-D{macro}")
        args.append(self.file_path)

        arg_str = " ".join(args)

        if not driver.parseCommandLine(arg_str):
            print("Error: Slang failed to parse the arguments.")
            return None

        if not driver.processOptions():
            print("Error: Slang failed to process the options.")
            return None

        if not driver.parseAllSources():
            print("Error: Slang failed to parse the sources.")
            return None

        return driver

    def parse(self):
        """Main entry point to parse SV code using pyslang AST."""
        self.modules = {}

        if not self.file_path:
            print("Error: No file path provided for ModParser.")
            return

        driver = self._run_slang()
        if not driver:
            return

        for tree in driver.syntaxTrees:
            root = tree.root

            for member in root.members:
                if "Module" not in member.kind.name:
                    continue

                mod_name = self._clean_token(member.header.name)
                self.modules[mod_name] = {
                    "parameters": {},
                    "localparams": {},
                    "ports": {}
                }
                mod_dict = self.modules[mod_name]

                # 1. Extract ANSI Parameters
                param_list = member.header.parameters
                if param_list and hasattr(param_list, "declarations"):
                    for param_decl in param_list.declarations:
                        self._process_parameter_list(param_decl, mod_dict)

                # 2. Extract Ports from header
                port_list = member.header.ports
                if port_list and hasattr(port_list, "ports"):
                    self._process_header_ports(port_list, mod_dict)

                # 3. Extract items from the Module Body
                if hasattr(member, "members"):
                    self._process_body_members(member.members, mod_dict)

    def get_names(self):
        """Get a list of modules names."""
        return list(self.modules.keys())

    def get_modules(self):
        """Get a dict with data extracted from modules."""
        return self.modules

    def get_module(self, module=None):
        """Get a dict with data extracted from one module."""
        if not module and len(self.modules) == 1:
            return next(iter(self.modules.values()))
        if module in self.modules:
            return self.modules[module]
        return None
