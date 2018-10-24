"""Return coordinates of free/open fields and the coordinates of the occupying armies.
"""

class KingdomSolver:

    def __init__(self):
        self.delta_coords = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        self.army_field = dict()
        
    def map_alpha(self, string_grid):
        """Return dictionary containing letter and coordinate pairs.
        """
        matrix = string_grid.split()
        
        for row_index, row in enumerate(matrix):
            for column_index, column in enumerate(row):
                if column.isalpha() and not column in self.army_field:
                    self.army_field[column] = [(row_index, column_index)]
                elif column.isalpha() and column in self.army_field:
                    self.army_field[column] += [(row_index, column_index)]

        return self.army_field

    def cross_check(self, coord, matrix):
        """Temporary function to be removed later if future function deems this one as obsolete.
        """
        max_row_len, max_column_len = len(matrix[0]) - 1, len(matrix) - 1
        row_index, column_index = coord

        if matrix[row_index][column_index].isalpha():
            set_ = set([(row_index + row, column_index + column) for row, column in self.delta_coords if
                        row_index + row >= 0 <= column_index + column and
                        row_index + row <= max_column_len and column_index + column <= max_row_len
                        and not matrix[row_index + row][column_index + column] == '#'])
            set_.add(coord)
            return set_
        else:
            return set()

    
