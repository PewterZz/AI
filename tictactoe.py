import math
import copy

class TicTacToe:
    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = 1

    def print_board(self):
        for row in self.state:
            print(" ".join(['X' if cell == 1 else 'O' if cell == -1 else ' ' for cell in row]))
            print("\n")

    def make_move(self, row, col):
        if self.state[row][col] == 0:
            self.state[row][col] = self.current_player
            self.current_player *= -1
            return True
        return False

    def terminal_node(self):
        for i in range(3):
            if self.state[i][0] == self.state[i][1] == self.state[i][2] != 0:
                return self.state[i][0]
            if self.state[0][i] == self.state[1][i] == self.state[2][i] != 0:
                return self.state[0][i]
        if self.state[0][0] == self.state[1][1] == self.state[2][2] != 0:
            return self.state[0][0]
        if self.state[0][2] == self.state[1][1] == self.state[2][0] != 0:
            return self.state[0][2]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return 0 
        return 0 

    def is_game_over(self):
        return self.terminal_node() != 0

def alphabeta(state, depth, alpha, beta, is_max_player):
    if depth == 0 or state.is_game_over():
        return state.terminal_node()

    if is_max_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if state.state[i][j] == 0:
                    state_copy = copy.deepcopy(state)
                    state_copy.make_move(i, j)
                    eval = alphabeta(state_copy, depth - 1, alpha, beta, False)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if state.state[i][j] == 0:
                    state_copy = copy.deepcopy(state)
                    state_copy.make_move(i, j)
                    eval = alphabeta(state_copy, depth - 1, alpha, beta, True)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(state):
    best_move = None
    best_eval = -math.inf
    for i in range(3):
        for j in range(3):
            if state.state[i][j] == 0:
                state_copy = copy.deepcopy(state)
                state_copy.make_move(i, j)
                eval = alphabeta(state_copy, 8, -math.inf, math.inf, False)
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

if __name__ == "__main__":
    game = TicTacToe()

    while not game.is_game_over():
        game.print_board()
        if game.current_player == 1:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if game.make_move(row, col):
                continue
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's turn...")
            best_move = find_best_move(game)
            game.make_move(best_move[0], best_move[1])

    game.print_board()
    winner = game.terminal_node()
    if winner == 0:
        print("It's a tie!")
    elif winner == 1:
        print("You win!")
    else:
        print("Computer wins!")
