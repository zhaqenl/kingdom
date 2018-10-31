"""File containing tests for core.py."""

from nose.tools import assert_equal
import core
import input_data

SOLVER_SIMPLE = core.KingdomSolver(input_data.simple_grid)
SOLVER_SIMPLE_2 = core.KingdomSolver(input_data.simple_grid_2)
SOLVER_EBZZRY = core.KingdomSolver(input_data.ebzzry_grid)

def test_valid_coord_false():
    """Test valid_coord on out of bound coordinate."""
    assert_equal(SOLVER_SIMPLE.valid_coord((4, 5)), False)

def test_valid_coord_true():
    """Test valid_coord on inside-bounded coordinate."""
    assert_equal(SOLVER_SIMPLE.valid_coord((4, 4)), True)

def test_coord_type_army():
    """Test coord_type on an army symbol."""
    assert_equal(SOLVER_SIMPLE.coord_type((3, 1)), 'army')

def test_coord_type_field():
    """Test coord_type on a field symbol."""
    assert_equal(SOLVER_SIMPLE.coord_type((3, 0)), 'field')

def test_flood_fill_field():
    """Test flood_fill on field symbol."""
    assert_equal(SOLVER_SIMPLE.flood_fill((3, 0)), None)

def test_flood_fill_army():
    """Test flood_fill on army symbol."""
    assert_equal(SOLVER_SIMPLE.flood_fill((1, 3)), [set([(1, 3), (2, 3), (3, 3), (2, 2), (2, 1),
                                                         (3, 1), (3, 0)])])

def test_flood_fill_valid_ebzzry():
    """Test flood_fill on army symbol (ebzzry_grid)."""
    assert_equal(SOLVER_EBZZRY.flood_fill((7, 12)), [set([(6, 12), (6, 13), (7, 12), (7, 13)])])

def test_map_army_field_simple():
    """Test map_army_field on simple_grid."""
    assert_equal(SOLVER_SIMPLE.map_army_field(),
                 {'e': [set([(1, 3), (3, 3), (3, 0), (3, 1), (2, 1), (2, 3), (2, 2)])],
                  'f': [set([(1, 3), (3, 3), (3, 0), (3, 1), (2, 1), (2, 3), (2, 2)]),
                        (set([(1, 3), (3, 3), (3, 0), (3, 1), (2, 1), (2, 3), (2, 2)]))]})

def test_map_army_count_simple():
    """Test map_army_count on simple_grid."""
    assert_equal(SOLVER_SIMPLE.map_army_count(), {'e': 1, 'f': 2})

def test_contested_simple():
    """Test contested on simple_grid."""
    assert_equal(SOLVER_SIMPLE.contested(), (1, {frozenset([(1, 3), (2, 3), (3, 3), (2, 2), (3, 0),
                                                            (3, 1), (2, 1)]): set(['e', 'f'])}))

def test_contested_simple_2():
    """Test contested on simple_grid_2."""
    assert_equal(SOLVER_SIMPLE_2.contested(), (2, {frozenset([(1, 3), (3, 4), (2, 4), (1, 4)]):
                                                   set(['e', 'f']),
                                                   frozenset([(3, 0), (3, 1)]): set(['a', 'f'])}))

def test_contested_ebzzry():
    """Test contested on ebzzry_grid."""
    assert_equal(SOLVER_EBZZRY.contested(), (1, {frozenset([(7, 9), (7, 8), (6, 8), (7, 10),
                                                            (7, 7)]): set(['e', 'd'])}))
