from nose.tools import *
import core
import input_data

solver = core.KingdomSolver()

def coord_match():
    pass

def test_find_alpha():
    assert_equal(solver.map_alpha(input_data.simple_grid), {'e': [(1, 3)]})

def test_cross_check():
    assert_equal(solver.cross_check((1, 1), input_data.simple_grid.split()), set())

def test_cross_check_zero_out():
    assert_equal(solver.cross_check((0, 0), input_data.simple_grid.split()), set())

def test_cross_check_army():
    assert_equal(solver.cross_check((1, 3), input_data.simple_grid.split()), set([(1, 3),
                                                                                (2, 3)]))

def test_explode_field_search():
    assert_equal(solver.explode_field_search((1, 3), input_data.simple_grid.split()),
                 set([(1, 3), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 3)]))

def snake_crawl():
    assert_equal(solver.snake_crawl((1, 3), input_data.simple_grid.split()),
                 set([(1, 3), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 3)]))
