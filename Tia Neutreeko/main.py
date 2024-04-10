import pygame
from time import sleep
import random  # Add this for the placeholder random move selection
from Neutreeko.constants import *
from Neutreeko.piece import *
from Neutreeko.board import *
from Neutreeko.wincon import *
from Neutreeko.messages import *
from Neutreeko.menu import *

# Main Function, code should be ran through here. Executes game.
def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tia Neutreeko!")
    bg = pygame.transform.scale(pygame.image.load('BackgroundOwO.png'), (window_width, window_height))
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    FPS = 15

    while True:
        draw_menu(screen, bg)
        pygame.display.update()
        selected_mode = None
        AI_player = 2  # Assuming AI is player 2

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if BUTTON_X <= mouse_x <= BUTTON_X + BUTTON_WIDTH:
                    for i, mode in enumerate(["Player vs. Player", "Player vs. AI", "AI vs. AI"]):
                        button_y = BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_GAP)
                        if button_y <= mouse_y <= button_y + BUTTON_HEIGHT:
                            selected_mode = mode
                            break

                    # Checks for selected mode then runs the game
                    if selected_mode == "Player vs. Player" or selected_mode == "Player vs. AI":
                        board = create_board()
                        previous_states = []
                        current_player = 1  # Player 1 starts
                        game_over = False
                        selected_piece = None

                        while not game_over:
                            clock.tick(FPS)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    return

                                # Player's turn (for both PvP and PvAI, since AI moves are handled separately)
                                if event.type == pygame.MOUSEBUTTONDOWN and current_player == 1:
                                    mouseX, mouseY = pygame.mouse.get_pos()
                                    col = int((mouseX - board_x) // square_size)
                                    row = int((mouseY - board_y) // square_size)

                                    if selected_piece is not None:
                                        if is_valid_move(board, selected_piece, (row, col)):
                                            move_piece(board, current_player, selected_piece, (row, col))
                                            draw_board(screen, board, bg)
                                            selected_piece = None
                                            previous_states.append(tuple(map(tuple, board)))
                                            if previous_states.count(tuple(map(tuple, board))) == 3:
                                                display_message(screen, "The game is a draw due to repetition.")
                                                game_over = True
                                                break
                                            if check_win(board, current_player):
                                                display_message(screen, f'Player {current_player} wins!')
                                                game_over = True
                                                break
                                            current_player = 2 if current_player == 1 else 1
                                        else:
                                            selected_piece = None  # Deselect the piece if the move is invalid
                                    else:
                                        # Select a piece
                                        if 0 <= row < rows and 0 <= col < cols and board[row][col] == current_player:
                                            selected_piece = (row, col)

                            # AI's turn
                            if selected_mode == "Player vs. AI" and current_player == AI_player and not game_over:
                                possible_moves = get_all_possible_moves(board, current_player)
                                selected_move = random.choice(possible_moves) if possible_moves else None

                                if selected_move:
                                    move_piece(board, current_player, selected_move[0], selected_move[1])
                                    draw_board(screen, board, bg)
                                    previous_states.append(tuple(map(tuple, board)))
                                    if previous_states.count(tuple(map(tuple, board))) == 3:
                                        display_message(screen, "The game is a draw due to repetition.")
                                        game_over = True
                                        break
                                    if check_win(board, current_player):
                                        display_message(screen, f'Player {current_player} wins!')
                                        game_over = True
                                        break
                                    current_player = 1  # Switch back to player 1

                            draw_board(screen, board, bg)
                            pygame.display.update()

if __name__ == '__main__':
    main()
