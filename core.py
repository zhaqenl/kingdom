"""Return coordinates of free/open fields and the coordinates of the occupying armies."""

class KingdomSolver(object):
    """Class."""

    def __init__(self, string_grid):
        """Initialize matrix."""
        if isinstance(string_grid, list):
            self.matrix = string_grid
        else:
            self.matrix = string_grid.split()

    def valid_coord(self, coord):
        """Return True if coord is within matrix bounds, False if not."""
        max_row = len(self.matrix) - 1
        max_column = len(self.matrix[0]) - 1
        row_index = coord[0]
        column_index = coord[1]

        if 0 <= row_index <= max_row and 0 <= column_index <= max_column:
            return True

        return False

    def coord_type(self, coord):
        """Return \'army\' if coord is of an army symbol, \'field\' if it is of a field symbol."""
        row_index = coord[0]
        column_index = coord[1]

        if self.valid_coord(coord) and self.matrix[row_index][column_index].isalpha():
            return 'army'
        elif self.valid_coord(coord) and self.matrix[row_index][column_index] == '.':
            return 'field'

        return None

    def flood_fill(self, coord):
        """Return set of field coordinates and army coordinates connected to coord."""
        delta_coords = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        pivots = [coord]
        collected_field = set()
        collected_army = set()

        if self.matrix[coord[0]][coord[1]] == '.':
            return None
        else:
            while pivots:
                curr_row, curr_column = pivots.pop(0)
                collected_field.add((curr_row, curr_column))
                for dir_ in delta_coords:
                    delta_row = dir_[0]
                    delta_column = dir_[1]
                    new_row = curr_row + delta_row
                    new_column = curr_column + delta_column
                    coord_type = self.coord_type((new_row, new_column))

                    if coord_type == 'field' and not (new_row, new_column) in collected_field:
                        collected_field.add((new_row, new_column))
                        pivots.append((new_row, new_column))

                    elif coord_type == 'army' and not (new_row, new_column) in collected_field:
                        collected_field.add((new_row, new_column))
                        collected_army.add((new_row, new_column))
                        pivots.append((new_row, new_column))

        return [collected_field]

    def map_army_field(self):
        """Return armies and their corresponding field coordinates."""
        army_field = dict()

        for row_index, row in enumerate(self.matrix):
            for column_index, column in enumerate(row):
                if column.isalpha() and not column in army_field:
                    army_field[column] = self.flood_fill((row_index, column_index))
                elif column.isalpha() and column in army_field:
                    army_field[column].extend(self.flood_fill((row_index, column_index)))

        return army_field

    def map_army_count(self):
        """Return armies and their corresponding count."""
        army_count = dict()

        for key, value in self.map_army_field().items():
            army_count[key] = len(value)

        return sorted(army_count.items())

    def contested(self):
        """Return contested fields with the corresponding contesting armies, and number of \
        contests."""
        army_dict = self.map_army_field()
        field_to_army = dict()
        contested_fields = dict()
        contested_ = 0

        for army, field_list in army_dict.items():
            for field in field_list:
                if not frozenset(field) in field_to_army:
                    field_to_army[frozenset(field)] = set([army])
                elif frozenset(field) in field_to_army:
                    field_to_army[frozenset(field)].update(set([army]))

        for field, armies in field_to_army.items():
            if len(armies) > 1:
                contested_ += 1

        for field, armies in field_to_army.items():
            if len(armies) != 1:
                contested_fields[field] = armies

        return contested_, contested_fields
