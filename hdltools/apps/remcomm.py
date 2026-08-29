#
# Copyright (C) 2026 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""This script removes comments from the original file."""

from hdltools.cli_parser import cli_parser
from hdltools.hdl_controller import HDLController

from hdltools.hdl_reader import HDLReader
from hdltools.hdl_writer import HDLWriter

args = cli_parser('comm')
reader = HDLReader()
reader.read_file(args.file)
raw_code = reader.get_code()
print(raw_code)
# writer = HDLWriter()
