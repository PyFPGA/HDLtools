#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
Sanitizes HDL source code by removing comments and extra whitespaces.
"""

import argparse
import re


class HdlSanitize:
    """Removes comments and extra whitespace in HDL (VHDL/Verilog) files."""

    def __init__(self, fpath, is_vhdl=False):
        try:
            with open(fpath, 'r', encoding='utf-8') as fobj:
                ftext = fobj.read()
        except (OSError, IOError) as error:
            self.code = f'Error opening {fpath}: {error}'
            return
        if is_vhdl:
            ftext = re.sub(r'--.*', '', ftext)
        else:
            ftext = re.sub(r'//.*', '', ftext)
            ftext = re.sub(r'/\*.*?\*/', '', ftext, flags=re.DOTALL)
        self.code = re.sub(r'\s+', ' ', ftext).strip()

    def get_code(self):
        """Get the sanitized HDL code."""
        return self.code

    def __str__(self):
        return self.code


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('hdlfile')
    args = parser.parse_args()
    code = HdlSanitize(args.hdlfile)
    print(code)
