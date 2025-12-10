from .cell import Cell, FixedSudokuCell, EditableSudokuCell


class SudokuGrid:
    def __init__(self, grid_size=3, grid_elements=[]):
        self._grid_size = grid_size
        self._cells: Cell = []

        if not grid_elements:
            raise ValueError("Elements cannot be empty")

        if len(grid_elements) != grid_size:
            raise Exception("Number of rows should match the grid size")

        for i in range(len(grid_elements)):
            row = grid_elements[i]

            if len(row) != grid_size:
                raise Exception("Number of columns should match the grid size")

            current_row = []

            for j in range(len(row)):
                val = row[j]
                if val == 0:
                    cell = EditableSudokuCell(grid_size)
                else:
                    cell = FixedSudokuCell(val, grid_size)

                current_row.append(cell)

            self._cells.append(current_row)

    def getValue(self, row, col):
        cell = self._cells[row][col]
        return cell.get_value()
