class SudokuCell:
    """The base class for any cell on the board."""

    def __init__(self, val=0, grid_size=3):
        if not isinstance(grid_size, int):
            raise TypeError("Grid size should be an integer")

        self._max_value: int = grid_size * grid_size

        if not isinstance(val, int):
            raise TypeError("Value should be an integer")

        if val != 0 and val < 1 or val > self._max_value:
            raise ValueError("Value must be in the range 1 - 9")

        self._value: int = val

    def get_value(self):
        return self._value

    def set_value(self, new_val):
        """Allows updates by default."""
        if not isinstance(new_val, int):
            raise TypeError("Value should be an integer")

        if new_val < 1 or new_val > self._max_value:
            raise ValueError("Value must be in the range 1 - 9")

        self._value = new_val

    def clear(self):
        self._value = 0


class PrepopulatedCell(SudokuCell):
    """A cell that cannot be updated."""

    def __init__(self, val, grid_size=3):
        # Call the parent class's initializer
        super().__init__(val, grid_size)

    def set_value(self, new_val):
        """Override the parent method to prevent updates."""
        raise PermissionError("Cannot change a fixed cell.")

    def clear(self):
        """Override the parent method to prevent clearing."""
        raise PermissionError("Cannot clear a fixed cell.")
