from pygame import *
from .constants import *
from .piece import *

#Creates the board for display on the screen

white =  pygame.transform.scale(pygame.image.load('WhitePiece.png'), (((board_height // 5.35)), ((board_width // 5.35))))
black =  pygame.transform.scale(pygame.image.load('BlackPiece.png'), (((board_height // 5.35)), ((board_width // 5.35))))
Tia = pygame.transform.scale(pygame.image.load('TiaMaid.png'), (500, 733))

#Draws the pieces on the board
def create_board():
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    board[0][1] = board[3][2] = board[0][3] = 1
    board[4][1] = board[1][2] = board[4][3] = 2
    return board

#Draws the board
def draw_board(screen, board, bg):

    screen.blit(bg, (0, 0))

    pygame.draw.rect(screen, board_color, (board_x-10, board_y-10, 20+cols * square_size, 20+rows * square_size), 7)

    for row in range(rows):
        for col in range(cols):
            # Create a semi-transparent surface
            piece_bg_tranparency = pygame.Surface((square_size, square_size))
            piece_bg_tranparency.set_alpha(100)  # Adjust alpha level

            board_bg_transparency = pygame.Surface((square_size, square_size))
            board_bg_transparency.set_alpha(60)

            board_bg_transparency.fill(pygame.Color('black'))  # Fill the surface with black color
            screen.blit(board_bg_transparency, (board_x + col * square_size, board_y + row * square_size)) 

            pygame.draw.rect(screen, board_color, (board_x + col * square_size + 1, board_y + row * square_size + 1, square_size - 2, square_size - 2), 2)
            
            piece = board[row][col]
            if piece == 1:
                piece_bg_tranparency.fill(pygame.Color('white'))  # Fill the surface of the white piece with white color
                screen.blit(piece_bg_tranparency, (board_x + col * square_size, board_y + row * square_size))  

                screen.blit(white, (4+board_x + col * square_size, 5+board_y + row * square_size))
            elif piece == 2:
                piece_bg_tranparency.fill(pygame.Color('black'))  # Fill the surface of the black piece with black color
                screen.blit(piece_bg_tranparency, (board_x + col * square_size, board_y + row * square_size))  

                screen.blit(black, (4+board_x + col * square_size, 5+board_y + row * square_size))
    
    character_x = 5
    character_y = (window_height - Tia.get_height()) //  2
    screen.blit(Tia, (character_x, character_y))

#Draws the possible moves
def draw_possible_moves(screen, board, selected_piece):
    if selected_piece is not None:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            row, col = selected_piece
            while 0 <= row+dx < rows and 0 <= col+dy < cols and board[row+dx][col+dy] == 0:
                row += dx
                col += dy
                if is_valid_move(board, selected_piece, (row, col)):
                    pygame.draw.circle(screen, (255, 255, 255), (board_x + col * square_size + square_size // 2, board_y + row * square_size + square_size // 2), 10)
