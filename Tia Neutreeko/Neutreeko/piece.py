from pygame import *
from .constants import *

#Function to allow for piece movement

def move_piece(board, player, start, end):
    start_row, start_col = start
    end_row, end_col = end
    
    # Check if the start position contains the player's piece
    if board[start_row][start_col] != player:
        return False

    # Check if the end position is empty
    if board[end_row][end_col] != 0:
        return False
    
    # Check if the move is valid
    if not is_valid_move(board, start, end):
        return False

    # Make the move
    board[start_row][start_col] = 0
    board[end_row][end_col] = player

    return True

#Check valid moves
def is_valid_move(board, start, end):
    start_row, start_col = start
    end_row, end_col = end

    # Check if the start and end positions are within the board bounds
    if not (0 <= start_row < rows and 0 <= start_col < cols and 0 <= end_row < rows and 0 <= end_col < cols):
        return False

    # Check if the start position contains the player's piece
    if board[start_row][start_col] == 0:
        return False

    # Check if the end position is empty
    if board[end_row][end_col] != 0:
        return False

    # Check if the move is in a straight line or diagonal
    if start_row != end_row and start_col != end_col and abs(start_row - end_row) != abs(start_col - end_col):
        return False

    # Check for obstruction along the path and if the end position is the farthest empty square
    delta_row = 1 if end_row > start_row else -1
    delta_col = 1 if end_col > start_col else -1

    if start_row == end_row:  # Horizontal move
        for col in range(start_col + delta_col, cols if delta_col == 1 else -1, delta_col):
            if board[start_row][col] != 0:
                return col - delta_col == end_col
    elif start_col == end_col:  # Vertical move
        for row in range(start_row + delta_row, rows if delta_row == 1 else -1, delta_row):
            if board[row][start_col] != 0:
                return row - delta_row == end_row
    else:  # Diagonal move
        for delta in range(1, min(rows, cols)):
            row = start_row + delta_row * delta
            col = start_col + delta_col * delta
            if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != 0:
                return row - delta_row == end_row and col - delta_col == end_col

    return True

# As funções abaixas são necessárias para o minimax existir, fazem parte do "Step 2" dentro do arquivo "algorithms.py"
# Function to identify all pieces for a given player
def get_player_pieces(board, player):
    pieces = []
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == player:
                pieces.append((row, col))
    return pieces

# Function to calculate all valid moves for a piece
def calculate_moves_for_piece(board, start_row, start_col):
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Up, Down, Left, Right, Diagonals

    for d_row, d_col in directions:
        row, col = start_row, start_col
        while True:
            row += d_row
            col += d_col
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 0:
                continue
            else:
                # Step back to the last valid position
                final_row, final_col = row - d_row, col - d_col
                if (final_row != start_row or final_col != start_col) and (0 <= final_row < rows and 0 <= final_col < cols):
                    moves.append(((start_row, start_col), (final_row, final_col)))
                break
    return moves

# Combine the above to find all moves for a player
def get_all_possible_moves(board, player):
    player_pieces = get_player_pieces(board, player)
    all_moves = []
    for start_pos in player_pieces:
        piece_moves = calculate_moves_for_piece(board, *start_pos)
        all_moves.extend(piece_moves)
    return all_moves
