#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""This script generates a stub for the specified module."""

import logging
import sys

from hdltools.cli_parser import cli_parser
from hdltools.hdl_reader import HDLReader
from hdltools.mod_parser import ModParser
from hdltools.hdl_writer import HDLWriter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

args = cli_parser('stub')

hdl_reader = HDLReader()
try:
    hdl_reader.read_file(args.file)
except:
    logging.error('file not found')
    sys.exit(1)
hdl_code = hdl_reader.get_code()

mod_parser = ModParser(hdl_code)
mod_parser.parse()

module_names = mod_parser.get_names()
if not len(module_names) or (args.top and args.top not in module_names):
    logging.error('module not found')
    sys.exit(1)

if not args.top:
    args.top = module_names[0]

module_info = mod_parser.get_module(args.top)
module_info['name'] = args.top
module_info['suffix'] = args.suffix

hdl_writer = HDLWriter()
hdl_writer.render('stub', module_info)

if not args.output:
    print(hdl_writer.get_code())
else:
    hdl_writer.write_file(args.output)
