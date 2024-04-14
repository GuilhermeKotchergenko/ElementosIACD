from Neutreeko.piece import *
from Neutreeko.wincon import *

def evaluate_easy(board, player):
    # Random evaluation to simulate easier games
    import random
    return random.randint(-10, 10)

# Hard and Medium difficulties
def evaluate_medium(board, player):
    score = 0
    opponent = 3 - player
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    max_score = 10000  

    # Immediate win check
    for x in range(5):
        for y in range(5):
            for dx, dy in directions:
                if x + 2*dx < 5 and y + 2*dy < 5 and x + 2*dx >= 0 and y + 2*dy >= 0:
                    if board[x][y] == player and board[x + dx][y + dy] == player and board[x + 2*dx][y + 2*dy] == player:
                        return max_score  # Immediate win for player
                    if board[x][y] == opponent and board[x + dx][y + dy] == opponent and board[x + 2*dx][y + 2*dy] == opponent:
                        return -max_score  # Block immediate win for opponent

    # Threat detection and blocking
    for x in range(5):
        for y in range(5):
            if board[x][y] == player or board[x][y] == opponent:
                current_player = board[x][y]
                for dx, dy in directions:
                    if x + 3*dx < 5 and y + 3*dy < 5 and x + 3*dx >= 0 and y + 3*dy >= 0:
                        if board[x + dx][y + dy] == current_player and board[x + 2*dx][y + 2*dy] == current_player and board[x + 3*dx][y + 3*dy] == 0:
                            if current_player == player:
                                score += 85
                            else:
                                score -= 100

    # Center control
    center_positions = [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
    for x, y in center_positions:
        if board[x][y] == player:
            score += 3
        elif board[x][y] == opponent:
            score -= 3

    return score

def minimax(board, depth, player, is_maximizing_player, evaluate_function, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or check_win(board, player):
        score = evaluate_function(board, player)
        print(f"Depth: {depth}, Score: {score}, Board: {board}")  # Debugging output
        return score, None

    if is_maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_possible_moves(board, player):
            new_board = [row[:] for row in board]
            move_piece(new_board, player, move[0], move[1])
            eval, _ = minimax(new_board, depth - 1, 3 - player, False, evaluate_function, alpha, beta)
            print(f"Maximizing - Player {player}: Move {move}, Eval {eval}")  # Debugging output
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_possible_moves(board, 3 - player):
            new_board = [row[:] for row in board]
            move_piece(new_board, 3 - player, move[0], move[1])
            eval, _ = minimax(new_board, depth - 1, player, True, evaluate_function, alpha, beta)
            print(f"Minimizing - Player {player}: Move {move}, Eval {eval}")  # Debugging output
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move
    
def get_evaluation_function(difficulty):
    if difficulty == "Easy":
        return evaluate_easy
    elif difficulty == "Medium":
        return evaluate_medium
    elif difficulty == "Hard":
        return evaluate_medium