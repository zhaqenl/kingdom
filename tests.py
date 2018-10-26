from nose.tools import *
import core
import input_data

solver = core.KingdomSolver()
matrix_simple = input_data.simple_grid.split()
matrix_ebzzry = input_data.ebzzry_grid.split()

def test_valid_coord_false():
    assert_equal(solver.valid_coord((4, 5), matrix_simple), False)

def test_valid_coord_true():
    assert_equal(solver.valid_coord((4, 4), matrix_simple), True)

def test_coord_type_army():
    assert_equal(solver.coord_type((3, 1), matrix_simple), 'army')

def test_coord_type_field():
    assert_equal(solver.coord_type((3, 0), matrix_simple), 'field')

def flood_fill_non_valid():
    assert_equal(solver.flood_fill((3, 1), matrix_simple), set())

def test_flood_fill_valid_simple():
    assert_equal(solver.flood_fill((1, 3), matrix_simple), ([set([(1, 3), (2, 3), (3, 3), (2, 2),
                                                                 (2, 1), (3, 1), (3, 0)])],
                                                            set([(3, 1), (2, 1)])))

def test_flood_fill_valid_ebzzry():
    assert_equal(solver.flood_fill((7, 12), matrix_ebzzry), ([set([(6, 12), (6, 13), (7, 12),
                                                                  (7, 13)])],
                                                             set([(7, 13)])))

def test_map_alpha_field_simple():
    assert_equal(solver.map_alpha_field(input_data.simple_grid),
                 {'e': ([set([(1, 3), (3, 3), (3, 0), (3, 1), (2, 1), (2, 3), (2, 2)])],
                         set([(3, 1), (2, 1)])),
                  'f': ([set([(1, 3), (3, 3), (3, 0), (3, 1), (2, 1), (2, 3), (2, 2)]),
                         (set([(1, 3), (3, 3), (3, 0), (3, 1), (2, 1), (2, 3), (2, 2)]))],
                         set([(1, 3), (3, 1)]))})
