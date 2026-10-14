#
# Copyright (C) 2025-2026 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
This module defines the HDLController class that orchestrates SystemVerilog
parsing (via pyslang) and output code generation (via Jinja2).
"""

import sys

from hdltools.mod_parser import ModParser
from hdltools.hdl_writer import HDLWriter


class HDLController:
    """Orchestrate SV parsing and template-based code generation tasks."""

    def __init__(self, template, defines=None):
        """Initializes controller."""
        self.parser = ModParser(defines=defines)
        self.writer = HDLWriter()
        self.template = template

    def generate(self, filepath, top=None, suffix=None):
        """Validates source, parses with slang, and renders output template."""

        try:
            # Check to ensure the file is accessible
            # before passing its path to the compiler driver.
            with open(filepath, 'r', encoding='utf-8') as f:
                f.read(1)
        except (OSError, UnicodeDecodeError):
            self._error(f'file not found or unreadable ({filepath})')

        self.parser.set_file(filepath)
        self.parser.parse()

        modules = self.parser.get_names()
        if not modules:
            self._error('no modules found or parsing failed')
        if top and top not in modules:
            self._error(f'top module not found ({top})')
        if not top:
            top = modules[0]

        context = self.parser.get_module(top)
        context['name'] = top
        context['suffix'] = suffix
        self.writer.render(self.template, context)

        return self.writer.get_code()

    def write(self, filepath):
        """Writes the generated code to a file, or stdout if empty."""
        if not filepath:
            print(self.writer.get_code())
        else:
            self.writer.write_file(filepath)

    @staticmethod
    def _error(message, ecode=1):
        """Logs an error message and terminates execution."""
        print(f'ERROR: {message}')
        sys.exit(ecode)
