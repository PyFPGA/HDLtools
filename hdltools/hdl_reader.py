#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
Reads and sanitizes the input HDL code by removing comments, extra whitespaces
and newlines.
"""

import re


class HDLReader:
    """Reads and sanitizes the input HDL code."""

    def __init__(self, code=''):
        self.code = code

    def read_file(self, path):
        """Reads the HDL code from file."""
        with open(path, 'r', encoding='utf-8') as fobj:
            self.code = fobj.read()

    def set_code(self, code):
        """Directly sets the HDL code."""
        self.code = code

    def is_vhdl(self):
        """Return True if the code seems to be VHDL."""
        return 'endmodule' not in self.code.lower()

    def get_code(self):
        """Retrieves the sanitized HDL code."""
        if self.is_vhdl():
            text = re.sub(r'--[^\n]*', '', self.code)
        else:
            text = re.sub(r'//[^\n]*', '', self.code)
            text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
        return re.sub(r'\s+', ' ', text).strip()
