#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
Module for detecting hardware description languages (HDL).

This module provides the `HdlDetect` class, which can detect whether a given
code is written in VHDL, Verilog, or SystemVerilog. It uses specific keywords
and patterns to identify the language based on the code provided.
"""

import argparse
import re


class HdlDetect:
    """
    Class to detect hardware description language (HDL) from a given code.
    """

    def __init__(self, code=''):
        self.lang = None
        self.detect(code)

    def detect(self, code):
        """Detect the HDL from the provided code."""
        self.code = code
        self.lang = None

        if 'entity' in self.code and 'module' not in self.code:
            self.lang = 'vhdl'
        elif 'entity' not in self.code and 'module' in self.code:
            self.lang = 'vlog'
            keywords = r'\blogic\b|\balways_ff\b|\balways_comb\b'
            if re.search(keywords, self.code):
                self.lang = 'slog'

    def is_vhdl(self):
        """Returns True if the code is VHDL."""
        return self.lang == 'vhdl'

    def is_vlog(self):
        """Returns True if the code is Verilog."""
        return self.lang == 'vlog'

    def is_slog(self):
        """Returns True if the code is SystemVerilog."""
        return self.lang == 'slog'

    def is_xlog(self):
        """Returns True if the code is Verilog or SystemVerilog."""
        return self.lang in ('vlog', 'slog')

    def get_lang(self):
        """Returns the detected language."""
        return self.lang

    def __str__(self):
        return self.lang


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('hdlfile')
    args = parser.parse_args()
    with open(args.hdlfile, 'r', encoding='utf-8') as fobj:
        text = fobj.read()
    obj = HdlDetect(text)
    print(obj.get_lang())
