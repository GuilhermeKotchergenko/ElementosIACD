from pygame import *
from .constants import *
from .board import *

def draw_menu(screen, bg):

    screen.blit(bg, (0, 0))

    #Button colors
    button_color = (128, 210, 242)
    button_hover_color = (184, 200, 209)

    #Draw buttons
    button_y = BUTTON_Y_START
    for mode in ["Player x Player", "Player x AI", "AI x AI"]:
        button_rect = pygame.Rect(BUTTON_X, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, button_color, button_rect, 0, 30)

        #Check if mouse is hovering over the button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, button_hover_color, button_rect, 0, 30)

        #Render button text
        font = pygame.font.Font('./Assets/Starborn.ttf', 40)
        text = font.render(mode, True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center) 
        screen.blit(text, text_rect)

        button_y += BUTTON_HEIGHT + BUTTON_GAP
    
    character_x = 5
    character_y = (window_height - Tia.get_height()) //  2
    screen.blit(Tia, (character_x, character_y))

    pygame.time.wait(10)
    pygame.display.flip()

def draw_difficulty_menu(screen, bg):

    screen.blit(bg, (0, 0))

    #Difficulty button colors
    button_color = (128, 210, 242)
    button_hover_color = (184, 200, 209)

    #Draw  difficulty buttons
    button_y = BUTTON_Y_START
    for mode in ["Easy", "Medium", "Hard"]:
        button_rect = pygame.Rect(BUTTON_X, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, button_color, button_rect, 0, 30)

        #Check if mouse is hovering over the button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, button_hover_color, button_rect, 0, 30)

        #Render button text
        font = pygame.font.Font('./Assets/Starborn.ttf', 40)
        text = font.render(mode, True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center) 
        screen.blit(text, text_rect)

        button_y += BUTTON_HEIGHT + BUTTON_GAP
    
    character_x = 5
    character_y = (window_height - Tia.get_height()) //  2
    screen.blit(Tia, (character_x, character_y))

    pygame.time.wait(10)
    pygame.display.flip()

def draw_AI_difficulty_menu(screen, bg, ai_label):
    running = True
    while running:
        screen.blit(bg, (0, 0))
        
        #Difficulty button colors
        button_color = (128, 210, 242)
        button_hover_color = (184, 200, 209)

        #Draw  difficulty buttons
        button_y = BUTTON_Y_START
        for diff in ["Easy", "Medium", "Hard"]:
            button_rect = pygame.Rect(BUTTON_X, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
            pygame.draw.rect(screen, button_color, button_rect, 0, 30)

            #Check if mouse is hovering over the button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(screen, button_hover_color, button_rect, 0, 30)

            #Render button text
            font = pygame.font.Font('./Assets/Starborn.ttf', 40)
            text = font.render(f"{ai_label} - {diff}", True, (255, 255, 255))
            text_rect = text.get_rect(center=button_rect.center) 
            screen.blit(text, text_rect)

            button_y += BUTTON_HEIGHT + BUTTON_GAP
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event. type == MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if BUTTON_X <= mouseX <= BUTTON_X + BUTTON_WIDTH:
                    for i, difficulty in enumerate(["Easy", "Medium", "Hard"]):
                        button_y = BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_GAP)
                        if button_y <= mouseY <= button_y + BUTTON_HEIGHT:
                            selected_difficulty = difficulty
                            running = False
                            break
        character_x = 5
        character_y = (window_height - Tia.get_height()) //  2
        screen.blit(Tia, (character_x, character_y))

        pygame.time.wait(10)
        pygame.display.flip()

    return selected_difficulty