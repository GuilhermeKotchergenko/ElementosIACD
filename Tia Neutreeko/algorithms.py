# Minimax:
# Step 1: Game State Evaluation Function
# score each game state from the perspective of the AI
# assign a high score to states where the AI is close to winning and a low score to states where the opponent is close to winning.

def evaluate(board, player):
    if check_win(board, player):
        return float('inf')  # Win
    elif check_win(board, 1 if player == 2 else 2):  # Check opponent win
        return float('-inf')  # Lose
    else:
        return 0  # Neutral

# Step 2: Generating Possible Moves
# Foram implementadas funções em  "piece.py", sendo elas: "get_player_pieces", "calculate_moves_for_piece" e "get_all_possible_moves"
# Foram implementadas adaptações em  "piece.py", para que:     Checking if it's the AI's turn; Generating all possible moves for the AI.   Selecting a move. (At this stage, you could randomly select a move from the possible moves as a placeholder until you implement the Minimax algorithm. Making the move. Switching the turn to the other player. 
