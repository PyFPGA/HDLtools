#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""This script compares two Verilog modules."""

import difflib
import sys

from hdltools.cli_parser import cli_parser
from hdltools.hdl_controller import HDLController


args = cli_parser('comp')
ctrl = HDLController('comp')
mod1 = ctrl.generate(args.files[0], args.top1)
mod2 = ctrl.generate(args.files[1], args.top2)

if mod1 == mod2:
    print('INFO: modules are equal')
else:
    print('ERROR: modules are different\n')
    diff = list(difflib.ndiff(mod1.splitlines(), mod2.splitlines()))
    print('\n'.join(diff))
    sys.exit(1)
