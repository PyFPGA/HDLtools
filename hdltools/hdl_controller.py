#
# Copyright (C) 2025-2026 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
This module defines the HDLController class that orchestrates the entire flow
from parsing modules, and generating output HDL code using Jinja2 templates.
"""

import sys

from hdltools.mod_parser import ModParser
from hdltools.hdl_writer import HDLWriter


class HDLController:
    """A central controller to orchestrate the HDL processing tasks."""

    def __init__(self, template):
        self.parser = ModParser()
        self.writer = HDLWriter()
        self.template = template

    def generate(self, filepath, top=None, suffix=None):
        """Generates HDL code from the input file."""

        try:
            # Quick check to ensure the file exists and is readable
            # before passing it to the slang driver.
            with open(filepath, 'r', encoding='utf-8') as f:
                f.read(1)
        except (OSError, UnicodeDecodeError):
            self._error(f'file not found or unreadable ({filepath})')

        self.parser.set_file(filepath)
        self.parser.parse()

        modules = self.parser.get_names()
        if not modules:
            self._error('module not found')
        if top and top not in modules:
            self._error(f'top not found ({top})')
        if not top:
            top = modules[0]

        context = self.parser.get_module(top)
        context['name'] = top
        context['suffix'] = suffix
        self.writer.render(self.template, context)

        return self.writer.get_code()

    def write(self, filepath):
        """Writes the generated HDL code."""
        if not filepath:
            print(self.writer.get_code())
        else:
            self.writer.write_file(filepath)

    @staticmethod
    def _error(message, ecode=1):
        print(f'ERROR: {message}')
        sys.exit(ecode)
