import argparse
import json
import re


class Modparse:

    def __init__(self, fpath):
        self.modules = {}
        with open(fpath, 'r') as f:
            self.ftext = f.read()
        self._remove_comments()
        self._parse()

    def _remove_comments(self):
        self.ftext = re.sub(r'//.*', '', self.ftext)
        self.ftext = re.sub(r'/\*.*?\*/', '', self.ftext, flags=re.DOTALL)

    def _parse(self):
        pattern = (
            r'module\s+'
            r'(\w+)\s*'             # name
            r'(?:#\(([^)]+)\))?\s*' # params
            r'\(([^)]*)\)\s*'       # ports
            r';\s*'
            r'.*?'                  # body
            r'endmodule'
        )
        matches = re.findall(pattern, self.ftext, re.DOTALL)
        for name, params, ports in matches:
            self.modules[name] = {}
            if params:
                self.modules[name]['params'] = self._extract_params(params)
            if ports:
                self.modules[name]['ports'] = self._extract_ports(ports)

    def _extract_params(self, text):
        pattern = (
            r'parameter\s+'
            r'(int|bit|logic|real|string)?\s*' # type
            r'(\[[^\]]*\])?\s*'                # packed
            r'(\w+)\s*'                        # name
            r'=\s*([^,;]+)'                    # value
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

    def _extract_ports(self, text):
        pattern = (
            r'(input|output|inout)\s+' # direction
            r'(reg|wire|logic)?\s*'    # type
            r'(signed|unsigned)?\s*'   # sign
            r'((?:\[[^\]]*\])*)\s*'    # packed
            r'(\w+)\s*'                # name
            r'((?:\[[^\]]*\])*)\s*'    # unpacked
            r'(?:=\s*([^,;]+))?'       # default
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
        return self.modules


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('svfile')
    args = parser.parse_args()
    parser = Modparse(args.svfile)
    modules = parser.get_modules()
    print(json.dumps(modules, indent=2))
