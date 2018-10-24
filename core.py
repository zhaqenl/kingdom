"""Return coordinates of free/open fields and the coordinates of the occupying armies.
"""

class KingdomSolver:

    def __init__(self):
        self.delta_coords = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.army_field = dict()
        
    def coord_field(self, coord, matrix):
        """Return True if coord is a field symbol, False if it is not.
        """
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        row_index = coord[0]
        column_index = coord[1]
        
        if 0 <= row_index <= max_row and 0 <= column_index <= max_column and \
        matrix[row_index][column_index] == '.':
            return True
        
        return False
    
    def coord_army(self, coord, matrix):
        """Return True if coord is an army symbol, False if it is not.
        """
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        row_index = coord[0]
        column_index = coord[1]

        if 0 <= row_index <= max_row and 0 <= column_index <= max_column and \
        matrix[row_index][column_index].isalpha():
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

    def flood_fill(self, coord, matrix):
        """Return set of field coordinates and army coordinates connected to coord.
        """
        pivots = [coord]
        collected_field = set()
        collected_army = set()
        
        while pivots:
            curr_row, curr_column = pivots.pop(0)
            collected_field.add((curr_row, curr_column))
            for dir_ in self.delta_coords:
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
