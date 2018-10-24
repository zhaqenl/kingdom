from nose.tools import *
import core
import input_data

solver = core.KingdomSolver()
matrix = input_data.simple_grid.split()

def test_find_alpha():
    assert_equal(solver.map_alpha(input_data.simple_grid), {'e': [(1, 3)]})

def test_cross_check():
    assert_equal(solver.cross_check((1, 1), matrix), set())

def test_cross_check_zero_out():
    assert_equal(solver.cross_check((0, 0), matrix), set())

def test_cross_check_army():
    assert_equal(solver.cross_check((1, 3), matrix), set([(1, 3), (2, 3)]))

def test_coord_valid_true():
    assert_equal(solver.coord_valid((3, 1), matrix), True)

def test_coord_valid_false():
    assert_equal(solver.coord_valid((3, 2), matrix), False)
