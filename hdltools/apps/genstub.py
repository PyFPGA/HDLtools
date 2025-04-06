#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""This script generates a stub for the specified module."""

from hdltools.cli_parser import cli_parser
from hdltools.hdl_controller import HDLController

args = cli_parser('wrap')
ctrl = HDLController('wrap')
code = ctrl.generate(args.file, args.top, args.suffix)

if not args.output:
    print(code)
else:
    ctrl.write(args.output)
