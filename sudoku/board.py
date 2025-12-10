from .cell import Cell, EditableSudokuCell, FixedSudokuCell


class SudokuBoard:
    def __init__(self, elements, board_size=3):
        self._grid_size = board_size
        self._max_dim = board_size * board_size

        self._cells: list[list[Cell]] = []

        if not elements:
            raise ValueError("Input elements list cannot be empty.")

        if len(elements) != self._max_dim:
            raise Exception(
                f"Number of rows ({len(elements)}) should match the board dimension ({self._max_dim}).")

        for row_data in elements:
            if len(row_data) != self._max_dim:
                raise Exception(
                    f"Number of columns ({len(row_data)}) should match the board dimension ({self._max_dim}).")

            current_cells_row = []

            for val in row_data:
                if val == 0:
                    cell = EditableSudokuCell(grid_size=self._grid_size)
                else:
                    cell = FixedSudokuCell(val, grid_size=self._grid_size)

                current_cells_row.append(cell)

            self._cells.append(current_cells_row)

    def __str__(self):
        """
        Defines the string representation of the SudokuBoard,
        allowing the use of 'print(board_instance)'.
        """
        output_lines = []

        max_dim = self._max_dim
        grid_size = self._grid_size

        # 1. Calculate the divider length
        temp_row_width = 2  # Left '|'
        temp_row_width += max_dim * 2  # Cells
        # Internal and final vertical bars
        temp_row_width += (max_dim // grid_size) * 2

        # Adjust for the extra space used in the original calculation
        # Subtract 1 for clean visual width
        divider = "-" * (temp_row_width - 1)

        output_lines.append("\n" + divider)

        for r in range(max_dim):
            row_output = "|"
            for c in range(max_dim):
                val = self.get_value(r, c)
                display_val = str(val) if val != 0 else " "
                row_output += f" {display_val}"

                # Add vertical dividers after every sub-grid column
                if (c + 1) % grid_size == 0:
                    row_output += " |"

            output_lines.append(row_output)

            # Add horizontal dividers after every sub-grid row
            if (r + 1) % grid_size == 0 and (r + 1) != max_dim:
                output_lines.append(divider)

        output_lines.append(divider + "\n")

        # Join all lines with a newline character and return the single string
        return "\n".join(output_lines)

    def get_value(self, row, col):
        if not (0 <= row < self._max_dim and 0 <= col < self._max_dim):
            raise IndexError("Row or column index is out of board bounds.")

        cell = self._cells[row][col]
        return cell.get_value()

    def place_number(self, row, col, num):
        """
        Sets the value of an editable cell. This is the solver's key writing tool.
        """
        if not (0 <= row < self._max_dim and 0 <= col < self._max_dim):
            raise IndexError("Indices are out of board bounds.")

        cell = self._cells[row][col]

        # The Cell class handles the validation (1-9 range) and PermissionError for Fixed cells.
        # We assume 'num' will be a valid 1-9 integer here.
        cell.set_value(num)

    def clear_number(self, row, col):
        """
        Clears an editable cell (sets its value to 0). Used for backtracking.
        """
        if not (0 <= row < self._max_dim and 0 <= col < self._max_dim):
            raise IndexError("Indices are out of board bounds.")

        cell = self._cells[row][col]

        # The Cell class handles the PermissionError for Fixed cells.
        cell.clear()

    def is_valid(self):
        ...
