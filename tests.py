from nose.tools import *
import core
import input_data

def test_find_alpha():
    assert_equal(core.find_alpha(input_data.my_test_grid), {'e': [(0, 1), (2, 1)]})

def test_cross_check():
    assert_equal(core.cross_check((1, 1), input_data.my_test_grid.split()), set([(0, 1), (1, 0),
                                                                                 (2, 1), (1, 1)]))

def test_cross_check_zero_out():
    assert_equal(core.cross_check((0, 0), input_data.my_test_grid.split()), set([(0, 1), (1, 0),
                                                                                 (0, 0)]))

def test_cross_check_strict():
    assert_equal(core.cross_check((2, 1), input_data.my_test_grid.split()), set([(2, 1), (2, 0),
                                                                                 (1, 1)]))

def test_cross_check_again():
    assert_equal(core.cross_check((1, 0), input_data.my_test_grid.split()), set([(1, 0), (1, 1),
                                                                                 (2, 0)]))

def field_check():
    assert_equal(core.field_check((0, 0), input_data.simple_grid.split()), set())


