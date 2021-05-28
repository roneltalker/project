import pygame
from buttons import options_screen


# shows the user a screen when the server checks the object in the image
def screen1():
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
    pygame.display.flip()

    green = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render('Scanning The Image...', True, green)
    textRect = text.get_rect()
    textRect.center = (350, 250)
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

    pygame.display.flip()


# shows the user a screen after the server checks the object in the image
def screen2(name):
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
    green = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 35)
    text = font.render('The object in the image is: ' + name, True, green)
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

    pygame.display.flip()
    # the buttons on the screen
    finish = False
    while not finish:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                finish = True
                return "exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 290 <= mouse[0] <= 290 + 150 and 290 <= mouse[1] <= 290 + 60:
                    return options_screen()
        if 290 <= mouse[0] <= 290 + 150 and 290 <= mouse[1] <= 290 + 60:
            pygame.draw.rect(screen, color_light, [290, 290, 150, 60])
        else:
            pygame.draw.rect(screen, color_dark, [290, 290, 150, 60])
        screen.blit(text, (298, 305))
        pygame.display.flip()
