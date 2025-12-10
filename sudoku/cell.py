from abc import ABC, abstractmethod


class Cell(ABC):
    """
    An Abstract Base Class (ABC) defining the required interface
    for any cell in the Sudoku structure.
    """

    def __init__(self, val=0, grid_size=3):
        if not isinstance(grid_size, int):
            raise TypeError("Grid size should be an integer")

        if not isinstance(val, int):
            raise TypeError("Value should be an integer")

        self._max_value: int = grid_size * grid_size

        if val != 0 and (val < 1 or val > self._max_value):
            raise ValueError(
                f"Value must be 0 or in the range 1 - {self._max_value}")

        self._value: int = val

    # Enforce these methods must exist in all derived classes
    @abstractmethod
    def set_value(self, new_val):
        """Must be implemented by child classes to set the cell's value."""
        pass

    @abstractmethod
    def clear(self):
        """Must be implemented by child classes to clear the cell."""
        pass

    # Concrete method (shared implementation)
    def get_value(self):
        return self._value


class EditableSudokuCell(Cell):
    """A cell whose value can be set and cleared (e.g., user input)."""

    def __init__(self, val=0, grid_size=3):
        # Calls the ABC's constructor for initialization and validation
        super().__init__(val, grid_size)

    # Implement the abstract method: set_value
    def set_value(self, new_val):
        """Allows updates by default, with validation."""
        if not isinstance(new_val, int):
            raise TypeError("Value should be an integer")

        # The max_value check now uses the inherited property
        if new_val < 1 or new_val > self._max_value:
            raise ValueError(
                f"Value must be in the range 1 - {self._max_value}")

        self._value = new_val

    # Implement the abstract method: clear
    def clear(self):
        """Sets the cell's value to 0 (empty)."""
        self._value = 0


class FixedSudokuCell(Cell):
    """A cell that is fixed and cannot be modified (e.g., puzzle clue)."""

    def __init__(self, val, grid_size=3):
        # Calls the ABC's constructor for initialization and validation
        super().__init__(val, grid_size)
        # Fixed cells should not be initialized as 0, the ABC check handles this.

    # Implement the abstract method: set_value (Prevents update)
    def set_value(self, new_val):
        """Override the parent method to prevent updates."""
        raise PermissionError("Cannot change a fixed cell.")

    # Implement the abstract method: clear (Prevents clearing)
    def clear(self):
        """Override the parent method to prevent clearing."""
        raise PermissionError("Cannot clear a fixed cell.")
