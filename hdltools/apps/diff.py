#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""This script checks differences between two Verilog modules."""

import argparse
import logging
import sys

from hdltools.mod_parse import ModParse


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

parser = argparse.ArgumentParser()
parser.add_argument('--top1')
parser.add_argument('--top2')
parser.add_argument('files', nargs=2)
args = parser.parse_args()

modules = ModParse(args.files[0])
module1 = modules.get_module(args.top1)
if not module1:
    logging.error('first module not found')
    sys.exit(1)

modules = ModParse(args.files[1])
module2 = modules.get_module(args.top2)
if not module2:
    logging.error('second module not found')
    sys.exit(1)

if module1 == module2:
    logging.info('modules are equal')
else:
    logging.error('modules have differences')
    sys.exit(1)
