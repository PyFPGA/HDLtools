#
# Copyright (C) 2025 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""This script generates a wrapper for the specified module."""

import argparse
import logging
import sys

from hdltools.mod_parse import ModParse
from hdltools.gen_file import GenFile


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

parser = argparse.ArgumentParser()
parser.add_argument('--top')
parser.add_argument('--suffix', default='_wrap')
parser.add_argument('--output')
parser.add_argument('file')
args = parser.parse_args()

modules = ModParse(args.file)
names = modules.get_names()

if not len(names) or (args.top and args.top not in names):
    logging.error('module not found')
    sys.exit(1)

if not args.top:
    args.top = names[0]

module = modules.get_module(args.top)
module['name'] = args.top
module['suffix'] = args.suffix

top = GenFile()
top.render('wrap', module)

if not args.output:
    print(top)
else:
    top.write(args.output)
