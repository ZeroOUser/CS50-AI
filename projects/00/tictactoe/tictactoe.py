"""
Tic Tac Toe Player
"""
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    totalX = 0
    totalO = 0
    for row in board:
        for cell in row:
            if cell == X:
                totalX += 1
            elif cell == O:
                totalO += 1
    if totalX > totalO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] != EMPTY:
        raise Exception("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_player = None
    n = len(board)
    m = len(board[0])

    # Check rows
    for row in range(n):
        if board[row][0] == EMPTY:
            continue
        if all(cell == board[row][0] for cell in board[row]):
            winning_player = board[row][0]
            break

    # Check columns
    for col in range(m):
        if all(row[col] == board[0][col] for row in board):
            winning_player = board[0][col]
            break

    # Check diagonals
    found_left = all(board[i][i] == board[0][0] for i in range(n))
    found_right = all(board[i][n - i - 1] == board[0][n - 1] for i in range(n))

    if found_left:
        winning_player = board[0][0]
    elif found_right:
        winning_player = board[0][n - 1]

    return winning_player


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    if winning_player == O:
        return -1
    return 0


def minimize(board):
    if terminal(board):
        return utility(board), None
    possible_moves = actions(board)
    min_value = float("inf")
    min_move = None
    for move in possible_moves:
        value = maximize(result(board, move))[0]
        if value < min_value:
            min_value = value
            min_move = move
    return min_value, min_move


def maximize(board):
    if terminal(board):
        return utility(board), None
    possible_moves = actions(board)
    max_value = float("-inf")
    max_move = None
    for move in possible_moves:
        value = minimize(result(board, move))[0]
        if value > max_value:
            max_value = value
            max_move = move
    return max_value, max_move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)
    if current_player == X:
        optimal_move = maximize(board)[1]
    else:
        optimal_move = minimize(board)[1]
    return optimal_move
