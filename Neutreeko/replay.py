from pygame import *
from .constants import *
from .board import *

#Blits the replay screen 

surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA)

def replay_screen(screen):

    pygame.draw.rect(surface, (255, 255, 255, 100), [0, 0, 1280, 800])
    screen.blit(surface, (0, 0))

    #Button colors
    button_color = (128, 210, 242)
    button_hover_color = (184, 200, 209)

    #Draw buttons
    button_y = BUTTON_Y_START
    for mode in ["<--"]:
        button_rect = pygame.Rect(BUTTON_X, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, button_color, button_rect, 0, 30)

        #Check if mouse is hovering over the button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_x, mouse_y):
            redraw = True
            pygame.draw.rect(screen, button_hover_color, button_rect, 0, 30)

        #Render button text
        font = pygame.font.Font('./Assets/Starborn.ttf', 40)
        text = font.render(mode, True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center) 
        screen.blit(text, text_rect)

        button_y += BUTTON_HEIGHT + BUTTON_GAP

    pygame.time.wait(10)
    pygame.display.flip()

