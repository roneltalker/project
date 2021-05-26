import pygame


# shows the tools screen
def options_screen():
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

    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    smallfont = pygame.font.Font('freesansbold.ttf', 40)
    text1 = smallfont.render('Filters', True, color)
    text2 = smallfont.render('Backgrounds', True, color)
    text3 = smallfont.render('Cut', True, color)
    text4 = smallfont.render('Frames', True, color)

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
    # the buttons on the screen
    finish = False
    while not finish:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 67 <= mouse[0] <= 67 + 280 and 84 <= mouse[1] <= 84 + 160:
                    return "filter"
                if 357 <= mouse[0] <= 357 + 280 and 84 <= mouse[1] <= 84 + 160:
                    return "background"
                if 67 <= mouse[0] <= 67 + 280 and 256 <= mouse[1] <= 256 + 160:
                    return "cut"
                if 357 <= mouse[0] <= 357 + 280 and 256 <= mouse[1] <= 256 + 160:
                    return "frame"
        if 67 <= mouse[0] <= 67 + 280 and 84 <= mouse[1] <= 84 + 160:
            pygame.draw.rect(screen, color_light, [67, 84, 280, 160])
        else:
            pygame.draw.rect(screen, color_dark, [67, 84, 280, 160])
        if 357 <= mouse[0] <= 357 + 280 and 84 <= mouse[1] <= 84 + 160:
            pygame.draw.rect(screen, color_light, [357, 84, 280, 160])
        else:
            pygame.draw.rect(screen, color_dark, [357, 84, 280, 160])
        if 67 <= mouse[0] <= 67 + 280 and 256 <= mouse[1] <= 256 + 160:
            pygame.draw.rect(screen, color_light, [67, 256, 280, 160])
        else:
            pygame.draw.rect(screen, color_dark, [67, 256, 280, 160])
        if 357 <= mouse[0] <= 357 + 280 and 256 <= mouse[1] <= 256 + 160:
            pygame.draw.rect(screen, color_light, [357, 256, 280, 160])
        else:
            pygame.draw.rect(screen, color_dark, [357, 256, 280, 160])
        screen.blit(text1, (142, 149))
        screen.blit(text2, (367, 149))
        screen.blit(text3, (160, 321))
        screen.blit(text4, (420, 321))
        pygame.display.flip()
