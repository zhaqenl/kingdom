"""Return coordinates of free/open fields and the coordinates of the occupying armies."""

class KingdomSolver(object):
    """Class."""

    @classmethod
    def valid_coord(cls, coord, matrix):
        """Return True if coord is within matrix bounds, False if not."""
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        row_index = coord[0]
        column_index = coord[1]

        if 0 <= row_index <= max_row and 0 <= column_index <= max_column:
            return True

        return False

    def coord_type(self, coord, matrix):
        """Return \'army\' if coord is of an army symbol, \'field\' if it is of a field symbol."""
        row_index = coord[0]
        column_index = coord[1]

        if self.valid_coord(coord, matrix) and matrix[row_index][column_index].isalpha():
            return 'army'
        elif self.valid_coord(coord, matrix) and matrix[row_index][column_index] == '.':
            return 'field'

        return None

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
                coord_type = self.coord_type((new_row, new_column), matrix)

                if coord_type == 'field' and not (new_row, new_column) in collected_field:
                    collected_field.add((new_row, new_column))
                    pivots.append((new_row, new_column))

                if coord_type == 'army' and not (new_row, new_column) in collected_field:
                    collected_field.add((new_row, new_column))
                    collected_army.add((new_row, new_column))
                    pivots.append((new_row, new_column))

        return [collected_field], collected_army

    def map_army_field(self, string_grid):
        """Return armies and their corresponding field coordinates."""
        matrix = string_grid.split()
        army_field = dict()

        for row_index, row in enumerate(matrix):
            for column_index, column in enumerate(row):
                if column.isalpha() and not column in army_field:
                    army_field[column] = self.flood_fill((row_index, column_index), matrix)
                elif column.isalpha() and column in army_field:
                    army_field[column][0].extend(self.flood_fill((row_index, column_index),
                                                                 matrix)[0])

        return army_field

    def map_army_count(self, string_grid):
        """Return armies and their corresponding count."""
        army_count = dict()

        for key, value in self.map_army_field(string_grid).items():
            army_count[key] = len(value[0])

        return army_count

    def contested(self, string_grid):
        """Return number of contested fields."""
        army_dict = self.map_army_field(string_grid)
        field_to_army = dict()
        contested_ = 0

        for army, field in army_dict.items():
            for occupied in field[0]:
                if not frozenset(occupied) in field_to_army:
                    field_to_army[frozenset(occupied)] = set([army])
                elif frozenset(occupied) in field_to_army:
                    field_to_army[frozenset(occupied)].update(set([army]))

        for field, armies in field_to_army.items():
            if len(armies) > 1:
                contested_ += 1

        return contested_
