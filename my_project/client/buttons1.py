import pygame
from crop import cutting
from frame import frames_screen1
from filters import filters_screen1
from background import cut


# contains the instructions
def options_instructions1(mes, button, category):
    pygame.init()
    if button == "filter":
        text = (pygame.font.Font('freesansbold.ttf', 35)).render('Choose the filter that you want', True, (255, 255, 255))
        return options_instructions2(mes, button, text, category)
    if button == "background":
        text1 = (pygame.font.Font('freesansbold.ttf', 35)).render('Crop the area of the object and', True, (255, 255, 255))
        text2 = (pygame.font.Font('freesansbold.ttf', 35)).render('choose the background that you want', True, (255, 255, 255))
        text = [text1, text2]
        return options_instructions2(mes, button, text, category)
    if button == "cut":
        text = (pygame.font.Font('freesansbold.ttf', 35)).render('Crop the image as you please', True, (255, 255, 255))
        return options_instructions2(mes, button, text, category)
    if button == "frame":
        text = (pygame.font.Font('freesansbold.ttf', 35)).render('Choose the frame that you want', True, (255, 255, 255))
        return options_instructions2(mes, button, text, category)


# shows the instructions screen
def options_instructions2(mes, button, text, category):
    # the graphics of the screen
    window_width = 700
    window_height = 500
    pygame.init()
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Image Design")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    color = (44, 118, 131)
    screen.fill(color)
    if button == "background":
        text1 = text[0]
        text2 = text[1]
        textRect1 = text1.get_rect()
        textRect1.center = (350, 150)
        screen.blit(text1, textRect1)
        textRect2 = text2.get_rect()
        textRect2.center = (350, 200)
        screen.blit(text2, textRect2)
    else:
        textRect = text.get_rect()
        textRect.center = (350, 150)
        screen.blit(text, textRect)

    x = 0
    y = 0
    while x < window_width:
        surf2 = pygame.Surface((20, 20))
        surf2.fill((0, 0, 0))
        screen.blit(surf2, (x, y))
        x = x + 1
    x = 0
    y = 0
    while y < window_height:
        surf2 = pygame.Surface((20, 20))
        surf2.fill((0, 0, 0))
        screen.blit(surf2, (x, y))
        y = y + 1
    x = 0
    y = window_height - 20
    while x < window_width:
        surf2 = pygame.Surface((20, 20))
        surf2.fill((0, 0, 0))
        screen.blit(surf2, (x, y))
        x = x + 1
    x = window_width - 20
    y = 0
    while y < window_height:
        surf2 = pygame.Surface((20, 20))
        surf2.fill((0, 0, 0))
        screen.blit(surf2, (x, y))
        y = y + 1

    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    smallfont = pygame.font.Font('freesansbold.ttf', 30)
    text = smallfont.render('Continue', True, color)

    # the buttons on the screen
    finish = False
    while not finish:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 290 <= mouse[0] <= 290 + 150 and 290 <= mouse[1] <= 290 + 60:
                    return options_instructions3(mes, button, category)
        if 290 <= mouse[0] <= 290 + 150 and 290 <= mouse[1] <= 290 + 60:
            pygame.draw.rect(screen, color_light, [290, 290, 150, 60])
        else:
            pygame.draw.rect(screen, color_dark, [290, 290, 150, 60])
        screen.blit(text, (298, 305))
        pygame.display.flip()

    pygame.display.flip()


# checks which tool the user has selected and operates accordingly
def options_instructions3(mes, button, category):
    if button == "filter":
        return filters_screen1(mes, category)
    if button == "background":
        return cut(mes, category)
    if button == "cut":
        return cutting(mes)
    if button == "frame":
        x = frames_screen1(mes)
        if x == "back1":
            return options_instructions3(mes, button, category)
        else:
            return x
