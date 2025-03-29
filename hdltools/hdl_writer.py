#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
Generates and writes the output HDL code based on templates.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class HDLWriter:
    """Generates and writes the output HDL code."""

    def __init__(self):
        tdir = Path(__file__).parent.joinpath('templates')
        self.env = Environment(loader=FileSystemLoader(str(tdir)))
        self.code = ''

    def render(self, tempname, context):
        """Render the specified template."""
        template = self.env.get_template(f'{tempname}.jinja')
        self.code = template.render(context)

    def write_file(self, path):
        """Writes the generated HDL code to the specified file."""
        with open(path, 'w', encoding='utf-8') as fobj:
            fobj.write(self.code)

    def get_code(self):
        """Get the generated code."""
        return self.code
