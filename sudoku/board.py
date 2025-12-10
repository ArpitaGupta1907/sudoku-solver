from .cell import Cell, EditableSudokuCell, FixedSudokuCell


class SudokuBoard:
    def __init__(self, board_size=3, elements=[]):
        self._board_size = board_size
        self._cells: Cell = []

        if not elements:
            raise ValueError("Elements cannot be empty")

        if len(elements) != board_size:
            raise Exception("Number of rows should match the grid size")

        for i in range(len(elements)):
            current_cells_row = []
            row = elements[i]

            for j in range(len(row)):
                if j == 0:
                    cell = EditableSudokuCell(board_size)
                else:
                    cell = FixedSudokuCell(row[j])

                current_cells_row.append(cell)

        self._cells.append(current_cells_row)

    def get_value(self, row, col):
        cell = self._cells[row][col]
        return cell.get_value()
