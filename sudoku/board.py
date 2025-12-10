from .cell import Cell, EditableSudokuCell, FixedSudokuCell


class SudokuBoard:
    def __init__(self, elements, board_size=3):
        self._grid_size = board_size
        self._max_dim = board_size * board_size

        # Corrected type hint
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

        print(
            f"SudokuBoard successfully initialized as a {self._max_dim}x{self._max_dim} puzzle.")

    def get_value(self, row, col):
        if not (0 <= row < self._max_dim and 0 <= col < self._max_dim):
            raise IndexError("Row or column index is out of board bounds.")

        cell = self._cells[row][col]
        return cell.get_value()
