#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""
Generates files based on templates.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class GenFile:
    """Generates files."""

    def __init__(self):
        tdir = Path(__file__).parent.joinpath('templates')
        self.env = Environment(loader=FileSystemLoader(str(tdir)))
        self.content = 'Nothing yet'

    def render(self, name, context):
        """Render the specified template."""
        template = self.env.get_template(f'{name}.jinja')
        self.content = template.render(context)

    def write(self, output):
        """Write content into a file."""
        with open(output, 'w', encoding='utf-8') as fobj:
            fobj.write(self.content)

    def __str__(self):
        return self.content
