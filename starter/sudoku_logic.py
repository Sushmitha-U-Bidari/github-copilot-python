import copy
import random

"""
Sudoku puzzle generation and validation utilities.

This module provides reusable helper functions for generating
Sudoku puzzles, solving boards, validating moves, counting
solutions, and creating puzzles with a unique solution.
"""

SIZE = 9
EMPTY = 0

def deep_copy(board):

    """
    Return a deep copy of the Sudoku board.
    """

    return copy.deepcopy(board)

def create_empty_board():

    """
    Create and return an empty 9×9 Sudoku board.
    """

    return [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]

def is_safe(board, row, col, num):

    """
    Check whether a number can be safely placed
    in the specified row and column.
    """

    # Check row and column.
    for index in range(SIZE):
        if board[row][index] == num or board[index][col] == num:
            return False

    # Check the 3x3 box.
    start_row = row - row % 3
    start_col = col - col % 3
    for row_offset in range(3):
        for col_offset in range(3):
            if board[start_row + row_offset][start_col + col_offset] == num:
                return False

    return True

def fill_board(board):

    """
    Fill the Sudoku board using a randomized
    backtracking algorithm.
    """

    for row_index in range(SIZE):
        for col_index in range(SIZE):
            if board[row_index][col_index] != EMPTY:
                continue

            # Randomize candidate values to generate different puzzles.
            candidates = list(range(1, SIZE + 1))
            random.shuffle(candidates)

            for candidate in candidates:
                if not is_safe(board, row_index, col_index, candidate):
                    continue

                board[row_index][col_index] = candidate

                # Continue recursively until the board is completely filled.
                if fill_board(board):
                    return True
                board[row_index][col_index] = EMPTY

            return False

    return True


def find_empty_cell(board):

    """
    Find and return the coordinates of the first
    empty cell on the board.
    """

    for row_index in range(SIZE):
        for col_index in range(SIZE):
            if board[row_index][col_index] == EMPTY:
                return row_index, col_index
    return None


def count_solutions(board, limit=2):

    """
    Count the number of valid Sudoku solutions.

    Stops searching once the specified limit
    has been reached.
    """

    empty_cell = find_empty_cell(board)
    if empty_cell is None:
        return 1

    row_index, col_index = empty_cell

    # Track the number of valid solutions found.
    solution_count = 0
    candidates = list(range(1, SIZE + 1))
    random.shuffle(candidates)

    for candidate in candidates:
        if not is_safe(board, row_index, col_index, candidate):
            continue

        board[row_index][col_index] = candidate
        solution_count += count_solutions(board, limit)
        board[row_index][col_index] = EMPTY

        if solution_count >= limit:
            return solution_count

    return solution_count


def remove_cells(board, clues):

    """
    Remove cells while ensuring the puzzle
    maintains exactly one valid solution.
    """

    cells_to_remove = SIZE * SIZE - clues

    # Create a randomized list of board positions.
    positions = [
        (row_index, col_index)
        for row_index in range(SIZE)
        for col_index in range(SIZE)
    ]
    random.shuffle(positions)

    for row_index, col_index in positions:
        if cells_to_remove <= 0:
            break

        if board[row_index][col_index] == EMPTY:
            continue

        original_value = board[row_index][col_index]
        board[row_index][col_index] = EMPTY

        # Restore the value if removing it results in
        # multiple possible solutions.
        if count_solutions(board, limit=2) != 1:
            board[row_index][col_index] = original_value
            continue

        cells_to_remove -= 1

def generate_puzzle(clues=35):

    """
    Generate a Sudoku puzzle along with its
    corresponding solved board.

    Returns:
        tuple: (puzzle, solution)
    """

    board = create_empty_board()

    # Generate a fully solved Sudoku board.
    fill_board(board)

    solution = deep_copy(board)
    puzzle = deep_copy(solution)

    # Remove cells to create the playable puzzle.
    remove_cells(puzzle, clues)
    return puzzle, solution
