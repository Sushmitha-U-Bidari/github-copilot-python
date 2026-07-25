from flask import Flask, render_template, jsonify, request
import sudoku_logic

app = Flask(__name__)

# Number of prefilled cells for each difficulty level.
DIFFICULTY_CLUES = {
    'easy': 45,
    'medium': 35,
    'hard': 28,
}

DEFAULT_CLUES = 35


# Stores the currently active puzzle and its solution.
# This allows the application to validate moves and
# generate hints during gameplay.

CURRENT = {
    'puzzle': None,
    'solution': None
}

# Validate that the incoming Sudoku board has the correct
# dimensions and contains only valid integer values.
def is_valid_board(board):

    """
    Validate that the supplied Sudoku board is a
    properly formatted 9×9 integer grid.
    """

    if not isinstance(board, list):
        return False

    if len(board) != sudoku_logic.SIZE:
        return False

    for row in board:
        if not isinstance(row, list):
            return False

        if len(row) != sudoku_logic.SIZE:
            return False

        for cell in row:
            if isinstance(cell, bool) or not isinstance(cell, int):
                return False

            if cell < 0 or cell > sudoku_logic.SIZE:
                return False

    return True

# Determine the number of clues based on the selected
# difficulty level or custom query parameter.
def resolve_clues():

    """
    Determine the number of clues based on the selected
    difficulty level or a custom query parameter.
    """

    difficulty = request.args.get('difficulty', '').strip().lower()
    if difficulty in DIFFICULTY_CLUES:
        return DIFFICULTY_CLUES[difficulty]

    clues = request.args.get('clues')
    if clues is not None:
        try:
            return int(clues)
        except (TypeError, ValueError):
            return DEFAULT_CLUES

    return DEFAULT_CLUES


@app.route('/')
def index():

    """
    Render the main Sudoku game page.
    """

    return render_template('index.html')

# Generate a new Sudoku puzzle and store both
# the puzzle and its solution for later validation.
@app.route('/new')
def new_game():

    """
    Generate a new Sudoku puzzle and store its solution.
    """

    clues = resolve_clues()
    puzzle, solution = sudoku_logic.generate_puzzle(clues)
    CURRENT['puzzle'] = puzzle
    CURRENT['solution'] = solution
    return jsonify({'puzzle': puzzle})

# Compare the player's current board with the
# stored solution and return correct and incorrect cells.
@app.route('/check', methods=['POST'])
def check_solution():
    
    """
    Compare the player's board with the stored solution
    and return the correct and incorrect cell positions.
    """

    data = request.get_json(silent=True)
    board = data.get('board') if isinstance(data, dict) else None
    solution = CURRENT.get('solution')
    puzzle = CURRENT.get('puzzle')

    if not is_valid_board(board):
        return jsonify({'error': 'A 9x9 board is required'}), 400

    if solution is None or puzzle is None:
        return jsonify({'error': 'No game in progress'}), 400

    incorrect = []
    correct = []

    # Compare only player-editable cells with the solution.
    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):
            if puzzle[i][j] != sudoku_logic.EMPTY:
                continue

            if board[i][j] == solution[i][j]:
                correct.append([i, j])
            else:
                incorrect.append([i, j])

    return jsonify({'incorrect': incorrect, 'correct': correct})

# Reveal exactly one correct value in an empty cell.
# Existing player-entered values are never overwritten.
@app.route('/hint', methods=['POST'])
def give_hint():

    """
    Reveal one correct value in an empty cell without
    overwriting player-entered values.
    """

    puzzle = CURRENT.get('puzzle')
    solution = CURRENT.get('solution')

    if puzzle is None or solution is None:
        return jsonify({'error': 'No game in progress'}), 400

    if request.is_json:
        data = request.get_json(silent=True)
        if data is None:
            return jsonify({'error': 'A 9x9 board is required'}), 400

        board = data.get('board') if isinstance(data, dict) else None
    else:
        board = None

    if board is None:
        board = puzzle

    if not is_valid_board(board):
        return jsonify({'error': 'A 9x9 board is required'}), 400

    # Reveal the first available empty cell.
    for row in range(sudoku_logic.SIZE):
        for col in range(sudoku_logic.SIZE):
            if board[row][col] == sudoku_logic.EMPTY:
                puzzle[row][col] = solution[row][col]
                return jsonify({
                    'row': row,
                    'col': col,
                    'value': solution[row][col]
                })

    return jsonify({'error': 'No empty cells available'}), 400


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)