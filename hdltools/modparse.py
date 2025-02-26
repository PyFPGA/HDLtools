import argparse
import json
import re


class Modparse:

    def __init__(self, file_path):
        self.file_path = file_path
        self.modules = {}
        self._parse()

    def _remove_comments(self, content):
        content = re.sub(r'//.*', '', content)
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        return content

    def _parse(self):
        with open(self.file_path, 'r') as f:
            content = f.read()
        content = self._remove_comments(content)
        pattern = r'module\s+(\w+)\s*(#\((.*?)\))?\s*\((.*?)\)\s*;'
        matches = re.findall(pattern, content, re.DOTALL)
        for match in matches:
            module_name = match[0]
            raw_parameters = match[2] if match[2] else ''
            raw_ports = match[3] if match[3] else ''
            parameters = self._extract_parameters(raw_parameters)
            ports = self._extract_ports(raw_ports)
            self.modules[module_name] = {}
            if parameters:
                self.modules[module_name]['parameters'] = parameters
            if ports:
                self.modules[module_name]['ports'] = ports

    def _extract_parameters(self, text):
        pattern = r'parameter\s+(int|bit|logic|real|string)?\s*(\[[^\]]*\])?\s*(\w+)\s*=\s*([^,;]+)'
        matches = re.findall(pattern, text)
        params = {}
        for param_type, packed, name, value in matches:
            params[name] = {}
            if param_type:
                params[name]['type'] = param_type
            if packed:
                params[name]['packed'] = packed
            if value:
                params[name]['value'] = value.strip()
        return params

    def _extract_ports(self, text):
        pattern = r'(input|output|inout)\s+(reg|wire|logic)?\s*(signed|unsigned)?\s*((?:\[[^\]]*\])*)\s*(\w+)\s*((?:\[[^\]]*\])*)\s*(?:=\s*([^,;]+))?'
        matches = re.findall(pattern, text)
        grouped_ports = {'inputs': {}, 'outputs': {}, 'inouts': {}}
        for direction, var_type, sign, packed, name, unpacked, default in matches:
            port_data = {}
            if var_type:
                port_data['type'] = var_type
            if sign:
                port_data['sign'] = sign
            if packed:
                port_data['packed'] = packed
            if unpacked:
                port_data['unpacked'] = unpacked
            if default:
                port_data['default'] = default.strip()
            grouped_ports[direction + 's'][name] = port_data  
        return {k: v for k, v in grouped_ports.items() if v}

    def get_modules(self):
        return self.modules


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('svfile')
    args = parser.parse_args()
    parser = Modparse(args.svfile)
    modules = parser.get_modules()
    print(json.dumps(modules, indent=2))
