import tkinter as tk
from PIL import Image, ImageOps, ImageTk
import pygame


# shows screen with buttons of the frames colors
def frames_screen1(im):
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

    color_light = (170, 170, 170)
    smallfont = pygame.font.Font('freesansbold.ttf', 30)

    text1 = smallfont.render('Black', True, (0, 0, 0))
    text2 = smallfont.render('Gray', True, (120, 120, 120))
    text3 = smallfont.render('Blue', True, (0, 0, 255))
    text4 = smallfont.render('Red', True, (255, 0, 0))
    text5 = smallfont.render('Green', True, (7, 90, 12))
    text6 = smallfont.render('Yellow', True, (213, 213, 0))
    text7 = smallfont.render('Purple', True, (109, 0, 119))
    text8 = smallfont.render('Pink', True, (198, 0, 99))
    text9 = smallfont.render('Orange', True, (234, 117, 0))
    text10 = smallfont.render('Brown', True, (102, 51, 0))
    color_light1 = (0, 0, 0)
    textt = smallfont.render('back', True, (255, 255, 255))

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
                if 50 <= mouse[0] <= 50 + 120 and 90 <= mouse[1] <= 90 + 50:
                    return frames_screen2(im, "black")
                if 210 <= mouse[0] <= 210 + 120 and 90 <= mouse[1] <= 90 + 50:
                    return frames_screen2(im, "gray")
                if 370 <= mouse[0] <= 370 + 120 and 90 <= mouse[1] <= 90 + 50:
                    return frames_screen2(im, "blue")
                if 530 <= mouse[0] <= 530 + 120 and 90 <= mouse[1] <= 90 + 50:
                    return frames_screen2(im, "red")
                if 50 <= mouse[0] <= 50 + 120 and 220 <= mouse[1] <= 220 + 50:
                    return frames_screen2(im, "green")
                if 210 <= mouse[0] <= 210 + 120 and 220 <= mouse[1] <= 220 + 50:
                    return frames_screen2(im, "yellow")
                if 370 <= mouse[0] <= 370 + 120 and 220 <= mouse[1] <= 220 + 50:
                    return frames_screen2(im, "purple")
                if 530 <= mouse[0] <= 530 + 120 and 220 <= mouse[1] <= 220 + 50:
                    return frames_screen2(im, "pink")
                if 210 <= mouse[0] <= 210 + 120 and 350 <= mouse[1] <= 350 + 50:
                    return frames_screen2(im, "orange")
                if 370 <= mouse[0] <= 370 + 120 and 350 <= mouse[1] <= 350 + 50:
                    return frames_screen2(im, "brown")
                if 50 <= mouse[0] <= 50 + 120 and 420 <= mouse[1] <= 420 + 50:
                    return "back"
        pygame.draw.rect(screen, color_light, [50, 90, 120, 50])
        pygame.draw.rect(screen, color_light, [210, 90, 120, 50])
        pygame.draw.rect(screen, color_light, [370, 90, 120, 50])
        pygame.draw.rect(screen, color_light, [530, 90, 120, 50])
        pygame.draw.rect(screen, color_light, [50, 220, 120, 50])
        pygame.draw.rect(screen, color_light, [210, 220, 120, 50])
        pygame.draw.rect(screen, color_light, [370, 220, 120, 50])
        pygame.draw.rect(screen, color_light, [530, 220, 120, 50])
        pygame.draw.rect(screen, color_light, [210, 350, 120, 50])
        pygame.draw.rect(screen, color_light, [370, 350, 120, 50])
        pygame.draw.rect(screen, color_light1, [50, 420, 120, 50])
        screen.blit(text1, (70, 100))
        screen.blit(text2, (235, 100))
        screen.blit(text3, (395, 100))
        screen.blit(text4, (560, 100))
        screen.blit(text5, (65, 230))
        screen.blit(text6, (220, 230))
        screen.blit(text7, (380, 230))
        screen.blit(text8, (560, 230))
        screen.blit(text9, (213, 360))
        screen.blit(text10, (383, 360))
        screen.blit(textt, (75, 430))
        pygame.display.flip()


# shows screen with buttons of the frames
def frames_screen2(img, color):
    # the graphics of the screen
    window_width = 700
    window_height = 500
    pygame.init()
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Image Design")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    color1 = (44, 118, 131)
    screen.fill(color1)

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

    smallfont = pygame.font.Font('freesansbold.ttf', 30)
    text1 = smallfont.render('1', True, (255, 255, 255))
    text2 = smallfont.render('2', True, (255, 255, 255))
    text3 = smallfont.render('3', True, (255, 255, 255))
    textt3 = smallfont.render('Choose & Exit', True, (0, 0, 0))
    textt2 = smallfont.render('Choose & Continue', True, (0, 0, 0))
    textt1 = smallfont.render('back', True, (0, 0, 0))

    pygame.display.flip()

    if color == "black":
        color_back = (0, 0, 0)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 1)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 2)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 3)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "gray":
        color_back = (120, 120, 120)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 4)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 5)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 6)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "blue":
        color_back = (0, 0, 255)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 7)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 8)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 9)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "red":
        color_back = (255, 0, 0)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 10)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 11)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 12)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "green":
        color_back = (7, 90, 12)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 13)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 14)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 15)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "yellow":
        color_back = (213, 213, 0)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 16)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 17)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 18)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "purple":
        color_back = (109, 0, 119)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 19)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 20)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 21)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "pink":
        color_back = (198, 0, 99)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 22)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 23)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 24)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "orange":
        color_back = (234, 117, 0)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 25)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 26)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 27)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()

    if color == "brown":
        color_back = (102, 51, 0)

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
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 28)
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 29)
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        frames_screen3(img, 30)
                    if 445 <= mouse[0] <= 445 + 220 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and exit"]
                        return arr
                    if 135 <= mouse[0] <= 135 + 300 and 340 <= mouse[1] <= 340 + 50:
                        x = frames_screen4(color)
                        arr = [x, "save and continue"]
                        return arr
                    if 40 <= mouse[0] <= 40 + 85 and 340 <= mouse[1] <= 340 + 50:
                        return "back1"
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [445, 340, 220, 50])
            pygame.draw.rect(screen, (255, 255, 255), [135, 340, 300, 50])
            pygame.draw.rect(screen, (255, 255, 255), [40, 340, 85, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            screen.blit(textt3, (450, 350))
            screen.blit(textt2, (140, 350))
            screen.blit(textt1, (45, 350))
            pygame.display.flip()


# shows the frames
def frames_screen3(img, number):
    # the window that opens with which the user sees each of the frames
    img = Image.open(img)
    img.thumbnail((250, 250))
    window = tk.Tk()
    window.title("Image Design")
    window.geometry("500x500")
    if number == 1:
        img1 = ImageTk.PhotoImage(frames(img, "black", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 2:
        img1 = ImageTk.PhotoImage(frames(img, "black", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 3:
        img1 = ImageTk.PhotoImage(frames(img, "black", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 4:
        img1 = ImageTk.PhotoImage(frames(img, "gray", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 5:
        img1 = ImageTk.PhotoImage(frames(img, "gray", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 6:
        img1 = ImageTk.PhotoImage(frames(img, "gray", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 7:
        img1 = ImageTk.PhotoImage(frames(img, "blue", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 8:
        img1 = ImageTk.PhotoImage(frames(img, "blue", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 9:
        img1 = ImageTk.PhotoImage(frames(img, "blue", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 10:
        img1 = ImageTk.PhotoImage(frames(img, "red", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 11:
        img1 = ImageTk.PhotoImage(frames(img, "red", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 12:
        img1 = ImageTk.PhotoImage(frames(img, "red", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 13:
        img1 = ImageTk.PhotoImage(frames(img, "green", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 14:
        img1 = ImageTk.PhotoImage(frames(img, "green", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 15:
        img1 = ImageTk.PhotoImage(frames(img, "green", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 16:
        img1 = ImageTk.PhotoImage(frames(img, "yellow", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 17:
        img1 = ImageTk.PhotoImage(frames(img, "yellow", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 18:
        img1 = ImageTk.PhotoImage(frames(img, "yellow", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 19:
        img1 = ImageTk.PhotoImage(frames(img, "purple", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 20:
        img1 = ImageTk.PhotoImage(frames(img, "purple", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 21:
        img1 = ImageTk.PhotoImage(frames(img, "purple", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 22:
        img1 = ImageTk.PhotoImage(frames(img, "pink", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 23:
        img1 = ImageTk.PhotoImage(frames(img, "pink", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 24:
        img1 = ImageTk.PhotoImage(frames(img, "pink", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 25:
        img1 = ImageTk.PhotoImage(frames(img, "orange", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 26:
        img1 = ImageTk.PhotoImage(frames(img, "orange", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 27:
        img1 = ImageTk.PhotoImage(frames(img, "orange", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 28:
        img1 = ImageTk.PhotoImage(frames(img, "brown", 10, 10, 10, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 29:
        img1 = ImageTk.PhotoImage(frames(img, "brown", 10, 20, 10, 20))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    if number == 30:
        img1 = ImageTk.PhotoImage(frames(img, "brown", 20, 10, 20, 10))
        panel = tk.Label(window, background="white", image=img1)
        panel.pack()
    window.mainloop()


# shows screen with buttons of the frames and the user need choose a frame
def frames_screen4(color):
    # the graphics of the screen
    window_width = 700
    window_height = 500
    pygame.init()
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Image Design")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    color1 = (44, 118, 131)
    screen.fill(color1)

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

    smallfont = pygame.font.Font('freesansbold.ttf', 30)
    text1 = smallfont.render('1', True, (255, 255, 255))
    text2 = smallfont.render('2', True, (255, 255, 255))
    text3 = smallfont.render('3', True, (255, 255, 255))

    pygame.display.flip()

    if color == "black":
        color_back = (0, 0, 0)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 1
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 2
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 3
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "gray":
        color_back = (120, 120, 120)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 4
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 5
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 6
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "blue":
        color_back = (0, 0, 255)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 7
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 8
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 9
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "red":
        color_back = (255, 0, 0)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 10
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 11
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 12
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "green":
        color_back = (7, 90, 12)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 13
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 14
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 15
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "yellow":
        color_back = (213, 213, 0)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 16
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 17
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 18
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "purple":
        color_back = (109, 0, 119)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 19
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 20
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 21
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "pink":
        color_back = (198, 0, 99)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 22
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 23
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 24
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "orange":
        color_back = (234, 117, 0)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 25
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 26
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 27
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()

    if color == "brown":
        color_back = (102, 51, 0)

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 28
                    if 300 <= mouse[0] <= 300 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 29
                    if 500 <= mouse[0] <= 500 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return 30
            pygame.draw.rect(screen, color_back, [100, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [300, 140, 120, 50])
            pygame.draw.rect(screen, color_back, [500, 140, 120, 50])
            screen.blit(text1, (150, 150))
            screen.blit(text2, (350, 150))
            screen.blit(text3, (550, 150))
            pygame.display.flip()


# creates frames
def frames(im, color, a, b, c, d):
    img = im
    border = (a, b, c, d)

    new_img = ImageOps.expand(img, border=border, fill=color)

    return new_img
