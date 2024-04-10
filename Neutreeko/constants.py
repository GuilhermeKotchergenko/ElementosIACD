import pygame

#window/board
window_width, window_height = 800, 600
board_width, board_height = 430, 430
rows, cols = 5, 5
square_size = board_width//cols
board_x = (window_width - board_width) // 1.2
board_y = (window_height - board_height) // 2

#colors
board_color = (237, 169, 90)
move_color = (255, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

#icon
icon = pygame.image.load('Logo32.png')

#Button
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_GAP = 20
BUTTON_X = (window_width - BUTTON_WIDTH) // 1.5
BUTTON_Y_START = 200

