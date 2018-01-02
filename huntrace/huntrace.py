# make code as python 3 compatible as possible
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import argparse
import functools
import subprocess
import sys

import hunter
from hunter import Q

PARSER = argparse.ArgumentParser(description='')
PARSER.add_argument('--depth', '-d', default=1, type=int, help='Print up to this depth of code')
PARSER.add_argument('--function', '-f', type=str, help='Trace this function', action='append')
PARSER.add_argument('--module', '-m', type=str, help='Trace this module', action='append')
PARSER.add_argument('command', nargs='+')


def main():
    args = PARSER.parse_args()
    path = subprocess.check_output(['which', args.command[0]]).strip('\n')
    sys.argv = args.command

    filters = []
    if args.function:
        for function in args.function:
            filters.append(Q(function=function))

    if args.module:
        for module in args.module:
            filters.append(Q(module=module, depth_lt=1000))

    if not filters:
        filters.append(Q(depth_lt=2 + args.depth, depth_gt=1, kind='line'))

    filter_q = functools.reduce(lambda a, b: a | b, filters)
    print(filter_q)
    with hunter.trace(filter_q):
        execfile(path)
