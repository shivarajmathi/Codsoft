#import package
import numpy as np

#players constraints 

# Constants for the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), EMPTY)
        self.current_player = PLAYER_X

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a win
        return (
            any(np.all(self.board[i, :] == player) for i in range(3)) or
            any(np.all(self.board[:, j] == player) for j in range(3)) or
            np.all(np.diag(self.board) == player) or
            np.all(np.diag(np.fliplr(self.board)) == player)
        )

    def is_full(self):
        return np.all(self.board != EMPTY)

    def make_move(self, row, col):
        if self.board[row, col] == EMPTY:
            self.board[row, col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

#aggrigating class
class TicTacToeAI:
    def minimax(self, board, depth, is_maximizing):
        if board.is_winner(PLAYER_O):
            return 1  # AI wins
        elif board.is_winner(PLAYER_X):
            return -1  # Human wins
        elif board.is_full():
            return 0  # Draw

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == EMPTY:
                        board.board[i][j] = PLAYER_O
                        score = self.minimax(board, depth + 1, False)
                        board.board[i][j] = EMPTY
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == EMPTY:
                        board.board[i][j] = PLAYER_X
                        score = self.minimax(board, depth + 1, True)
                        board.board[i][j] = EMPTY
                        best_score = min(score, best_score)
            return best_score

    def find_best_move(self, board):
        best_score = float('-inf')
        move = (-1, -1)
        
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == EMPTY:
                    board.board[i][j] = PLAYER_O
                    score = self.minimax(board, 0, False)
                    board.board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        
        return move

#function statements
def main():
    game = TicTacToe()
    ai = TicTacToeAI()

    while True:
        game.print_board()
        
        # Human player's turn
        row, col = map(int, input("Enter your move (row and column): ").split())
        
        if not game.make_move(row - 1, col - 1):  # Adjusting for zero-indexing
            print("Invalid move. Try again.")
            continue
        
        if game.is_winner(PLAYER_X):
            game.print_board()
            print("Congratulations! You win!")
            break
        
        if game.is_full():
            game.print_board()
            print("It's a draw!")
            break
        
        # AI's turn
        print("AI is making a move...")
        ai_move = ai.find_best_move(game)
        
        if ai_move != (-1, -1):
            game.make_move(ai_move[0], ai_move[1])
        
        if game.is_winner(PLAYER_O):
            game.print_board()
            print("AI wins! Better luck next time.")
            break
        
        if game.is_full():
            game.print_board()
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    main()

