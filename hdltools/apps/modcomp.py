#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""This script compares two Verilog modules."""

import difflib
import logging
import sys

from hdltools.cli_parser import cli_parser
from hdltools.hdl_reader import HDLReader
from hdltools.mod_parser import ModParser
from hdltools.hdl_writer import HDLWriter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

args = cli_parser('comp')

#
# Module 1
#

hdl_reader = HDLReader()
try:
    hdl_reader.read_file(args.files[0])
except (OSError, UnicodeDecodeError) as e:
    logging.error(f'{e}')
    sys.exit(1)
hdl_code = hdl_reader.get_code()

mod_parser = ModParser(hdl_code)
mod_parser.parse()

module_names = mod_parser.get_names()
if not len(module_names) or (args.top1 and args.top1 not in module_names):
    logging.error('first module not found')
    sys.exit(1)

if not args.top1:
    args.top1 = module_names[0]

module_info = mod_parser.get_module(args.top1)
module_info['name'] = args.top1

hdl_writer = HDLWriter()
hdl_writer.render('comp', module_info)

module1 = hdl_writer.get_code()

#
# Module 2
#

hdl_reader = HDLReader()
try:
    hdl_reader.read_file(args.files[1])
except (OSError, UnicodeDecodeError) as e:
    logging.error(f'{e}')
    sys.exit(1)
hdl_code = hdl_reader.get_code()

mod_parser = ModParser(hdl_code)
mod_parser.parse()

module_names = mod_parser.get_names()
if not len(module_names) or (args.top2 and args.top2 not in module_names):
    logging.error('second module not found')
    sys.exit(1)

if not args.top2:
    args.top2 = module_names[0]

module_info = mod_parser.get_module(args.top2)
module_info['name'] = args.top2

hdl_writer = HDLWriter()
hdl_writer.render('comp', module_info)

module2 = hdl_writer.get_code()

#
# Diff
#

if module1 == module2:
    logging.info('modules are equal')
else:
    logging.error('modules have differences')
    diff = list(difflib.ndiff(module1.splitlines(), module2.splitlines()))
    print("\n".join(diff))
    sys.exit(1)
