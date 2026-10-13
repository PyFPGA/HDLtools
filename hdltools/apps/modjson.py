#
# Copyright (C) 2026 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""Print collected info as JSON."""

import json

from hdltools.cli_parser import cli_parser
from hdltools.mod_parser import ModParser


args = cli_parser()
parser = ModParser(args.file, defines=args.defines)
parser.parse()
data = parser.get_modules()
print(json.dumps(data, indent=4))
