"""Return coordinates of free/open fields and the coordinates of the occupying armies."""

class KingdomSolver(object):
    """Class."""

    @classmethod
    def coord_field(cls, coord, matrix):
        """Return True if coord is a field symbol, False if it is not."""
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        row_index = coord[0]
        column_index = coord[1]

        if 0 <= row_index <= max_row and 0 <= column_index <= max_column and \
        matrix[row_index][column_index] == '.':
            return True

        return False

    @classmethod
    def coord_army(cls, coord, matrix):
        """Return True if coord is an army symbol, False if it is not."""
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        row_index = coord[0]
        column_index = coord[1]

        if 0 <= row_index <= max_row and 0 <= column_index <= max_column and \
        matrix[row_index][column_index].isalpha():
            return True

        return False

    @classmethod
    def map_alpha(cls, string_grid):
        """Return dictionary containing letter and coordinate pairs."""
        matrix = string_grid.split()
        army_field = dict()

        for row_index, row in enumerate(matrix):
            for column_index, column in enumerate(row):
                if column.isalpha() and not column in army_field:
                    army_field[column] = [(row_index, column_index)]
                elif column.isalpha() and column in army_field:
                    army_field[column] += [(row_index, column_index)]

        return army_field

    def flood_fill(self, coord, matrix):
        """Return set of field coordinates and army coordinates connected to coord."""
        delta_coords = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        pivots = [coord]
        collected_field = set()
        collected_army = set()

        while pivots:
            curr_row, curr_column = pivots.pop(0)
            collected_field.add((curr_row, curr_column))
            for dir_ in delta_coords:
                delta_row = dir_[0]
                delta_column = dir_[1]
                new_row = curr_row + delta_row
                new_column = curr_column + delta_column

                if self.coord_field((new_row, new_column), matrix) and not (new_row, new_column) \
                in collected_field:
                    collected_field.add((new_row, new_column))
                    pivots.append((new_row, new_column))

                if self.coord_army((new_row, new_column), matrix) and not (new_row, new_column) \
                in collected_field:
                    collected_field.add((new_row, new_column))
                    collected_army.add((new_row, new_column))
                    pivots.append((new_row, new_column))

        return collected_field, collected_army
