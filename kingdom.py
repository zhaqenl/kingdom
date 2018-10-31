"""python kingdom.py FILE.

This script is for handling specialized kingdom input files. The format for the input file is the
following:

'Number of cases'
'String grid height'
'String grid width'
'String grid'
...
...
...
"""

import sys
import argparse
import core

PARSER = argparse.ArgumentParser()
PARSER.add_argument('filename')
ARGS = PARSER.parse_args()

with open(ARGS.filename) as f:
    CASE_COUNT = f.readline().strip('\n')
    for case in xrange(int(CASE_COUNT)):
        sys.stdout.write('Case ')
        sys.stdout.write(str(case + 1))
        sys.stdout.write(':\n')
        grid = []
        grid_height_limit = int(f.readline().strip('\n'))
        grid_width = int(f.readline().strip('\n'))
        for _ in xrange(grid_height_limit):
            grid += [f.readline().strip('\n')]
        solver = core.KingdomSolver(grid)
        contested_ = solver.contested()[0]
        for key, value in sorted(solver.map_army_count().items()):
            print key, value
        if contested_ != 0:
            sys.stdout.write('contested ')
            print contested_
    sys.stdout.flush()
