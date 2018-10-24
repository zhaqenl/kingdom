"""Return coordinates of free/open fields and the coordinates of the occupying armies.
"""

class KingdomSolver:

    def __init__(self):
        self.delta_coords = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.army_field = dict()
        self.collected = []
        self.pivots = []
        
    def coord_valid(self, coord, matrix):
        """Return True if coord is not a mountain symbol, False if it is.
        """
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        
        row_index = coord[0]
        column_index = coord[1]
        if 0 <= row_index <= max_row and 0 <= column_index <= max_column and \
        matrix[row_index][column_index] != '#' and not coord in self.collected:
            return True
        return False

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
            set_ = set([(row_index + row, column_index + column) for row, column in
                        self.delta_coords if row_index + row >= 0 <= column_index + column and
                        row_index + row <= max_column_len and column_index + column <= max_row_len
                        and not matrix[row_index + row][column_index + column] == '#'])
            set_.add(coord)
            return set_
        else:
            return set()

    def flood_fill(self, coord, matrix):
        """Return the coordinates connected to coord.
        """
        self.pivots = [coord]
        
        while self.pivots:
            curr_row, curr_column = self.pivots.pop(0)
            self.collected += [(curr_row, curr_column)]
            for dir_ in self.delta_coords:
                x, y = dir_[0], dir_[1]
                new_row, new_column = curr_row + x, curr_column + y
                if self.coord_valid((new_row, new_column), matrix):
                    self.collected += [(new_row, new_column)]
                    self.pivots.append((new_row, new_column))

        return set(self.collected)
