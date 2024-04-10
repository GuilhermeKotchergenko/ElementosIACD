import pygame
from time import sleep
from Neutreeko.constants import *
from Neutreeko.piece import *
from Neutreeko.board import *
from Neutreeko.wincon import *
from Neutreeko.messages import *
from Neutreeko.menu import *


#Main Function, code should be ran trought here. Executes game.

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tia Neutreeko!")
    bg = pygame.transform.scale(pygame.image.load('Background.png'), (window_width, window_height))
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    FPS = 15

    while True:
        draw_menu(screen, bg)
        pygame.display.update()

        clock.tick(FPS)
        selected_mode = None

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event. type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if BUTTON_X <= mouse_x <= BUTTON_X + BUTTON_WIDTH:
                    for i, mode in enumerate(["Player x Player", "Player x AI", "AI x AI"]):
                        button_y = BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_GAP)
                        if button_y <= mouse_y <= button_y + BUTTON_HEIGHT:
                            selected_mode = mode
                            break

                    #Checks for selected mode then runs the game   
                    if selected_mode == "Player x Player":
                        board = create_board() 
                        draw_board(screen, board, bg)
                        previous_states = [] #Checks for repetition
                        current_player = 2
                        game_over = False
                        selected_piece = None

                        while not game_over:
                            clock.tick(FPS)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    return 
                                elif event.type == pygame.MOUSEBUTTONDOWN:
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
                                                display_messagedraw(screen, "DRAW!")
                                                game_over = True
                                            if check_win(board, current_player):
                                                display_messagewin(screen, f'{"Black" if current_player == 2 else "White"} wins!')
                                                game_over = True
                                            current_player = 2 if current_player == 1 else 1
                                        else:
                                            if 0 <= row < rows and 0 <= col < cols and board[row][col] == current_player:
                                                draw_board(screen, board, bg)
                                                selected_piece = (row, col)
                                                draw_possible_moves(screen, board, selected_piece)  
                                    else:
                                        #Select a piece
                                        if 0 <= row < rows and 0 <= col < cols and board[row][col] == current_player:
                                            draw_board(screen, board, bg)
                                            selected_piece = (row, col)
                                            draw_possible_moves(screen, board, selected_piece)
                            
                            pygame.display.update()
                            
        pygame.display.update()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()