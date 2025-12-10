from sudoku import SudokuBoard, SudokuSolver
from constants import EASY_BOARD, MEDIUM_BOARD, HARD_BOARD

easyBoard = SudokuBoard(EASY_BOARD, 3)
mediumBoard = SudokuBoard(MEDIUM_BOARD, 3)
hardBoard = SudokuBoard(HARD_BOARD, 3)

print(easyBoard)
print(mediumBoard)
print(hardBoard)

solver = SudokuSolver()

solver.solve(easyBoard)
solver.solve(mediumBoard)
solver.solve(hardBoard)
