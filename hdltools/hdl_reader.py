#
# Copyright (C) 2025-2026 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
Reads and sanitizes the input HDL code by removing comments, trailing espaces
and multiple empty lines.
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

    def get_code(self):
        """Retrieves the sanitized HDL code."""
        text = self.code
        text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
        if self._is_vhdl(text):
            text = re.sub(r'--.*', '', text)
        else:
            text = re.sub(r'//.*', '', text)
        text = re.sub(r'[ \t]+$', '', text, flags=re.MULTILINE)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def _is_vhdl(self, text):
        """Heuristic to determine if the code is VHDL or Verilog."""
        vhdl_score = 0
        vlog_score = 0

        vhdl_keywords = r'\b(library|entity|architecture|signal|begin)\b'
        vlog_keywords = r'\b(endmodule|assign|logic|wire|reg|parameter)\b'

        vhdl_matches = re.findall(vhdl_keywords, text, re.IGNORECASE)
        vhdl_score += len(set(vhdl_matches))

        vlog_matches = re.findall(vlog_keywords, text)
        vlog_score += len(set(vlog_matches))

        return vhdl_score > vlog_score
