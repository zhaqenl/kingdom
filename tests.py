from nose.tools import *
import core
import input_data

solver = core.KingdomSolver()
matrix_simple = input_data.simple_grid.split()
matrix_ebzzry = input_data.ebzzry_grid.split()

def test_find_alpha():
    assert_equal(solver.map_alpha(input_data.simple_grid), {'e': [(1, 3)], 'f': [(3, 1)]})

def test_coord_field_true():
    assert_equal(solver.coord_field((3, 0), matrix_simple), True)

def test_coord_field_false():
    assert_equal(solver.coord_field((3, 2), matrix_simple), False)

def test_coord_army_false():
    assert_equal(solver.coord_army((1, 7), matrix_ebzzry), False)

def test_coord_army_true():
    assert_equal(solver.coord_army((1, 8), matrix_ebzzry), True)

def flood_fill_non_valid():
    assert_equal(solver.flood_fill((3, 1), matrix_simple), set())

def test_flood_fill_valid():
    assert_equal(solver.flood_fill((1, 3), matrix_simple), (set([(1, 3), (2, 3), (3, 3), (2, 2),
                                                                 (2, 1), (3, 1), (3, 0)]),
                                                            set([(3, 1)])))
