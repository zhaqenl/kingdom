"""Return coordinates of free/open fields and the coordinates of the occupying armies.
"""

def find_alpha(string_grid):
    matrix = string_grid.split()
    army_field = dict()
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if column.isalpha() and not column in army_field:
                army_field[column] = [(row_index, column_index)]
            elif column.isalpha() and column in army_field:
                army_field[column] += [(row_index, column_index)]
    return army_field

def cross_check(coord, matrix):
    max_row_len, max_column_len = len(matrix[0]) - 1, len(matrix) - 1
    delta_coords = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    row_index, column_index = coord
    set_ = set([(row_index + row, column_index + column) for row, column in delta_coords
                if row_index + row >= 0 <= column_index + column and
                row_index + row <= max_column_len and column_index + column <= max_row_len and
                not matrix[row_index + row][column_index + column] == '#'])
    set_.update([coord])
    return set_

def field_check(coord, matrix):
    pass
