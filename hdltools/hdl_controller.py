#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
This module defines the HDLController class that orchestrates the entire flow
from reading and sanitizing HDL code, parsing modules, and generating output
HDL code using Jinja2 templates.
"""

import sys

from hdltools.hdl_reader import HDLReader
from hdltools.mod_parser import ModParser
from hdltools.hdl_writer import HDLWriter


class HDLController:
    """A central controller to orchestrate the HDL processing tasks."""

    def __init__(self, template):
        self.reader = HDLReader()
        self.parser = ModParser()
        self.writer = HDLWriter()
        self.template = template

    def generate(self, filepath, top=None, suffix=None):
        """Generates HDL code from the input file."""

        try:
            self.reader.read_file(filepath)
        except (OSError, UnicodeDecodeError):
            self._error(f'file not found ({filepath})')

        raw_code = self.reader.get_code()
        self.parser.set_code(raw_code)
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
