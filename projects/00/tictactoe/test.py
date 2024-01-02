from tictactoe import terminal
from tictactoe import winner
X = "X"
O = "O"
EMPTY = None

board = [[X, X, EMPTY],
         [X, EMPTY, EMPTY],
         [X, EMPTY, EMPTY]]

print(winner(board))
print(terminal(board))