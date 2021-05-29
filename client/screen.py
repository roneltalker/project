import pygame
from file import i
import sys
from PyQt5.QtWidgets import *


# shows the user the opening screen
def first_screen():
    # the graphics of the screen
    window_width = 700 # the width of the window
    window_height = 500 # the width of the window
    pygame.init()
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size) # creates the window
    pygame.display.set_caption("Image Design") # the name of the window (the name of the project)
    icon = pygame.image.load("images/icon.png") # the icon of the window
    pygame.display.set_icon(icon)
    color = (44, 118, 131) # the color of the screen background
    screen.fill(color)
    # the graphic in the center of the screen
    surf = pygame.Surface((90, 90))
    surf.fill((0, 0, 0))
    screen.blit(surf, (300, 200))
    surf1 = pygame.Surface((75, 75))
    surf1.fill(color)
    screen.blit(surf1, (307.5, 207.5))
    pygame.draw.circle(screen, (0, 0, 0), (345, 250), 20)
    pygame.draw.circle(screen, color, (345, 250), 12)
    pygame.draw.circle(screen, (0, 0, 0), (373, 220), 7)
    # the black line in the top side of the screen
    x = 0
    y = 0
    while x < window_width:
        surf2 = pygame.Surface((20, 20))
        surf2.fill((0, 0, 0))
        screen.blit(surf2, (x, y))
        x = x + 1
    # the black line in the left side of the screen
    x = 0
    y = 0
    while y < window_height:
        surf2 = pygame.Surface((20, 20))
        surf2.fill((0, 0, 0))
        screen.blit(surf2, (x, y))
        y = y + 1
    # the black line in the bottom side of the screen
    x = 0
    y = window_height - 20
    while x < window_width:
        surf2 = pygame.Surface((20, 20))
        surf2.fill((0, 0, 0))
        screen.blit(surf2, (x, y))
        x = x + 1
    # the black line in the right side of the screen
    x = window_width - 20
    y = 0
    while y < window_height:
        surf2 = pygame.Surface((20, 20))
        surf2.fill((0, 0, 0))
        screen.blit(surf2, (x, y))
        y = y + 1

    white = (255, 255, 255) # the color of the project name and the subheading
    font = pygame.font.SysFont('Corbel', 60) # the font of the project name
    text = font.render('Image Design', True, white) # the project name
    textRect = text.get_rect()
    textRect.center = (350, 80) # the location of the project name
    screen.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', 25) # the font of the subheading
    text = font.render('By Machine Learning', True, color, white) # the subheading
    textRect = text.get_rect()
    textRect.center = (350, 125) # the location of the subheading
    screen.blit(text, textRect)

    color1 = (255, 255, 255) # the color of the text button
    color_light = (170, 170, 170) # the color of the button when the mouse on it
    color_dark = (100, 100, 100) # the color of the button when the mouse doesn't on it
    smallfont = pygame.font.Font('freesansbold.ttf', 30) # the font of the text button
    text = smallfont.render('Exit', True, color1) # the text button
    smallfont1 = pygame.font.Font('freesansbold.ttf', 20) # the font of the text button
    text1 = smallfont1.render('Select an image you want to edit', True, color1) # the text button

    pygame.display.flip()
    # the buttons on the screen
    finish = False
    while not finish:
        mouse = pygame.mouse.get_pos() # the position of the mouse cursor
        # all events of the user
        for event in pygame.event.get():
            # if the user clicked on the X, the software is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                finish = True
                return 'exit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the user clicked on the "Exit" button, the software is closed
                if 295 <= mouse[0] <= 295 + 100 and 400 <= mouse[1] <= 400 + 40:
                    pygame.quit()
                    finish = True
                    return 'exit'
                # if the user clicked on the choose image button
                if 185 <= mouse[0] <= 185 + 330 and 330 <= mouse[1] <= 330 + 40:
                    app = QApplication(sys.argv) # application that create an object with a list of arguments from a cmd
                    l = i() # list of the image's details
                    print(l)
                    li = l[-1]
                    print(li)
                    return li # the image's location
                    app.exec_()
        if 295 <= mouse[0] <= 295 + 100 and 400 <= mouse[1] <= 400 + 40:
            pygame.draw.rect(screen, color_light, [295, 400, 100, 40])
        else:
            pygame.draw.rect(screen, color_dark, [295, 400, 100, 40])
        if 185 <= mouse[0] <= 185 + 330 and 330 <= mouse[1] <= 330 + 40:
            pygame.draw.rect(screen, color_light, [185, 330, 330, 40])
        else:
            pygame.draw.rect(screen, color_dark, [185, 330, 330, 40])
        screen.blit(text, (315, 405)) # the location of the text button
        screen.blit(text1, (190, 335)) # the location of the text button
        pygame.display.flip()
