#
# Copyright (C) 2025-2026 HDLtools Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""This file implements the command-line parser."""

import argparse


def cli_parser(app=None):
    """Parse command-line arguments based on the selected application."""

    parser = argparse.ArgumentParser()

    if app == 'comp':
        parser.add_argument('--top1')
        parser.add_argument('--top2')
    elif app in ['stub', 'wrap']:
        parser.add_argument('--top')
        parser.add_argument('--suffix', default=f'_{app}')
        parser.add_argument('--output')

    if app == 'comp':
        parser.add_argument('files', nargs=2)
    else:
        parser.add_argument('file')

    return parser.parse_args()
