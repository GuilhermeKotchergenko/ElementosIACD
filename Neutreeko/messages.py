from pygame import *
from .constants import *

#Display the winning message.

def display_message(screen, msg):
    font = pygame.font.Font(None, 36)
    text = font.render(msg, True, (0, 0, 0))
    screen.blit(text, ((window_width - text.get_width()) // 1.45, (window_height - text.get_height()) // 15))
    pygame.display.update()
    pygame.time.wait(2000)