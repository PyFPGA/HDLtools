#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
Parses SystemVerilog modules to extract information about parameters and ports.
"""

import argparse
import json
import re

from hdltools.hdl_sanitize import HdlSanitize


class ModParse:
    """Extract information about parameters and ports from modules."""

    def __init__(self, fpath):
        self.modules = {}
        hdl = HdlSanitize(fpath)
        self.code = hdl.get_code()
        self._parse()

    def _parse(self):
        pattern = (
            r'module\s+'
            r'(\w+)\s*'        # name
            r'(#\(.*?\))?\s*'  # params
            r'\((.*?)\)\s*;'   # ports
            r'.*?endmodule'
        )
        matches = re.findall(pattern, self.code, re.DOTALL)
        for name, params, ports in matches:
            self.modules[name] = {}
            if params:
                self.modules[name]['params'] = self._extract_params(params)
            if ports:
                self.modules[name]['ports'] = self._extract_ports(ports)

    @staticmethod
    def _extract_params(text):
        text = re.sub(r'[#()]', '', text)
        pattern = (
            r'parameter\s+'
            r'(int|bit|logic|real|string)?\s*'  # type
            r'(\[[^\]]*\])?\s*'                 # packed
            r'(\w+)\s*'                         # name
            r'=\s*([^,;]+)'                     # value
        )
        matches = re.findall(pattern, text)
        params = {}
        for ptype, packed, name, value in matches:
            params[name] = {}
            if ptype:
                params[name]['type'] = ptype
            if packed:
                params[name]['packed'] = packed
            if value:
                params[name]['value'] = value.strip()
        return params

    @staticmethod
    def _extract_ports(text):
        pattern = (
            r'(input|output|inout)\s+'  # direction
            r'(reg|wire|logic)?\s*'     # type
            r'(signed|unsigned)?\s*'    # sign
            r'((?:\[[^\]]*\])*)\s*'     # packed
            r'(\w+)\s*'                 # name
            r'((?:\[[^\]]*\])*)\s*'     # unpacked
            r'(?:=\s*([^,;]+))?'        # default
        )
        matches = re.findall(pattern, text)
        grouped_ports = {'inputs': {}, 'outputs': {}, 'inouts': {}}
        for pdir, ptype, sign, packed, name, unpacked, default in matches:
            data = {}
            if ptype:
                data['type'] = ptype
            if sign:
                data['sign'] = sign
            if packed:
                data['packed'] = packed
            if unpacked:
                data['unpacked'] = unpacked
            if default:
                data['default'] = default.strip()
            grouped_ports[pdir + 's'][name] = data
        return {k: v for k, v in grouped_ports.items() if v}

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

    def __str__(self):
        return json.dumps(self.modules, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('svfile')
    args = parser.parse_args()
    modules = ModParse(args.svfile)
    print(modules)
