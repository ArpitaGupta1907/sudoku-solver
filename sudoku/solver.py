from .board import SudokuBoard


class SudokuSolver:
    def is_valid(self, board: SudokuBoard) -> bool:
        ...

    def solve(self, board: SudokuBoard) -> None:
        ...
