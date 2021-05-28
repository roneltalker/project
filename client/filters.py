import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageChops
import numpy as np
import pygame


# converts the image to a binary image
def get_binary_image(im,threshold):
    grayscale = im.convert(mode='L') # black-white image
    arr = np.array(grayscale)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] >= threshold:
                arr[i][j] = 255
            else:
                arr[i][j] = 0
    return Image.fromarray(arr) # constructs an image from a numbers array


# shows screen with buttons of the filters by categories
def filters_screen1(im, category):
    # the graphics of the screen
    window_width = 900
    window_height = 600
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

    if category == "person":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Flip', True, (255, 255, 255))
        text2 = smallfont.render('Black-White', True, (255, 255, 255))
        text3 = smallfont.render('Black-White-Contours', True, (255, 255, 255))
        text4 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text5 = smallfont.render('Light', True, (255, 255, 255))
        text6 = smallfont.render('Water-Color', True, (255, 255, 255))
        text7 = smallfont.render('Contrast', True, (255, 255, 255))
        text8 = smallfont.render('Darkness', True, (255, 255, 255))
        color_light1 = (0, 0, 0)
        textt3 = smallfont.render('Choose & Exit', True, (255, 255, 255))
        textt2 = smallfont.render('Choose & Continue', True, (255, 255, 255))
        textt1 = smallfont.render('back', True, (255, 255, 255))

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
                    if 210 <= mouse[0] <= 210 + 55 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "flip")
                    if 540 <= mouse[0] <= 540 + 180 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "black-white")
                    if 80 <= mouse[0] <= 80 + 325 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "black-white contours")
                    if 490 <= mouse[0] <= 490 + 300 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "increasing contours")
                    if 200 <= mouse[0] <= 200 + 75 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "light")
                    if 545 <= mouse[0] <= 545 + 180 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "water color")
                    if 170 <= mouse[0] <= 170 + 130 and 360 <= mouse[1] <= 360 + 50:
                        filters_screen2(im, "contrast")
                    if 560 <= mouse[0] <= 560 + 145 and 360 <= mouse[1] <= 360 + 50:
                        filters_screen2(im, "darkness")
                    if 595 <= mouse[0] <= 595 + 225 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("person")
                        arr = [x, "save and exit"]
                        return arr
                    if 225 <= mouse[0] <= 225 + 310 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("person")
                        arr = [x, "save and continue"]
                        return arr
                    if 65 <= mouse[0] <= 65 + 95 and 490 <= mouse[1] <= 490 + 50:
                        return "back"
            pygame.draw.rect(screen, color_light, [210, 60, 55, 50])
            pygame.draw.rect(screen, color_light, [540, 60, 180, 50])
            pygame.draw.rect(screen, color_light, [80, 160, 325, 50])
            pygame.draw.rect(screen, color_light, [490, 160, 300, 50])
            pygame.draw.rect(screen, color_light, [200, 260, 75, 50])
            pygame.draw.rect(screen, color_light, [545, 260, 180, 50])
            pygame.draw.rect(screen, color_light, [170, 360, 130, 50])
            pygame.draw.rect(screen, color_light, [560, 360, 145, 50])
            pygame.draw.rect(screen, color_light1, [595, 490, 225, 50])
            pygame.draw.rect(screen, color_light1, [225, 490, 310, 50])
            pygame.draw.rect(screen, color_light1, [65, 490, 95, 50])
            screen.blit(text1, (210, 70))
            screen.blit(text2, (540, 70))
            screen.blit(text3, (80, 170))
            screen.blit(text4, (490, 170))
            screen.blit(text5, (200, 270))
            screen.blit(text6, (545, 270))
            screen.blit(text7, (170, 370))
            screen.blit(text8, (560, 370))
            screen.blit(textt3, (605, 500))
            screen.blit(textt2, (235, 500))
            screen.blit(textt1, (75, 500))
            pygame.display.flip()

    if category == "vehicle":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Flip', True, (255, 255, 255))
        text2 = smallfont.render('Black-White', True, (255, 255, 255))
        text3 = smallfont.render('Contours', True, (255, 255, 255))
        text4 = smallfont.render('Red', True, (255, 255, 255))
        text5 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text6 = smallfont.render('Night', True, (255, 255, 255))
        text7 = smallfont.render('Dark', True, (255, 255, 255))
        text8 = smallfont.render('Water-Color', True, (255, 255, 255))
        text9 = smallfont.render('Contrast', True, (255, 255, 255))
        text10 = smallfont.render('Black-White-Binary', True, (255, 255, 255))
        text11 = smallfont.render('High-Increasing-Contours', True, (255, 255, 255))
        text12 = smallfont.render('High-Darkness', True, (255, 255, 255))
        color_light1 = (0, 0, 0)
        textt3 = smallfont.render('Choose & Exit', True, (255, 255, 255))
        textt2 = smallfont.render('Choose & Continue', True, (255, 255, 255))
        textt1 = smallfont.render('back', True, (255, 255, 255))

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
                    if 100 <= mouse[0] <= 100 + 55 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "flip")
                    if 250 <= mouse[0] <= 250 + 180 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "black-white")
                    if 520 <= mouse[0] <= 520 + 135 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "contours")
                    if 750 <= mouse[0] <= 750 + 60 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "red")
                    if 115 <= mouse[0] <= 115 + 300 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "increasing contours")
                    if 555 <= mouse[0] <= 555 + 80 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "night")
                    if 745 <= mouse[0] <= 745 + 75 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "dark")
                    if 100 <= mouse[0] <= 100 + 180 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "water color")
                    if 350 <= mouse[0] <= 350 + 130 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "contrast")
                    if 540 <= mouse[0] <= 540 + 290 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "black-white binary")
                    if 80 <= mouse[0] <= 80 + 380 and 360 <= mouse[1] <= 360 + 50:
                        filters_screen2(im, "high increasing contours")
                    if 560 <= mouse[0] <= 560 + 220 and 360 <= mouse[1] <= 360 + 50:
                        filters_screen2(im, "high darkness")
                    if 595 <= mouse[0] <= 595 + 225 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("vehicle")
                        arr = [x, "save and exit"]
                        return arr
                    if 225 <= mouse[0] <= 225 + 310 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("vehicle")
                        arr = [x, "save and continue"]
                        return arr
                    if 65 <= mouse[0] <= 65 + 95 and 490 <= mouse[1] <= 490 + 50:
                        return "back"
            pygame.draw.rect(screen, color_light, [100, 60, 55, 50])
            pygame.draw.rect(screen, color_light, [250, 60, 180, 50])
            pygame.draw.rect(screen, color_light, [520, 60, 135, 50])
            pygame.draw.rect(screen, color_light, [750, 60, 60, 50])
            pygame.draw.rect(screen, color_light, [115, 160, 300, 50])
            pygame.draw.rect(screen, color_light, [555, 160, 80, 50])
            pygame.draw.rect(screen, color_light, [745, 160, 75, 50])
            pygame.draw.rect(screen, color_light, [100, 260, 180, 50])
            pygame.draw.rect(screen, color_light, [350, 260, 130, 50])
            pygame.draw.rect(screen, color_light, [540, 260, 290, 50])
            pygame.draw.rect(screen, color_light, [80, 360, 380, 50])
            pygame.draw.rect(screen, color_light, [560, 360, 220, 50])
            pygame.draw.rect(screen, color_light1, [595, 490, 225, 50])
            pygame.draw.rect(screen, color_light1, [225, 490, 310, 50])
            pygame.draw.rect(screen, color_light1, [65, 490, 95, 50])
            screen.blit(text1, (100, 70))
            screen.blit(text2, (250, 70))
            screen.blit(text3, (520, 70))
            screen.blit(text4, (750, 70))
            screen.blit(text5, (115, 170))
            screen.blit(text6, (555, 170))
            screen.blit(text7, (745, 170))
            screen.blit(text8, (100, 270))
            screen.blit(text9, (350, 270))
            screen.blit(text10, (540, 270))
            screen.blit(text11, (80, 370))
            screen.blit(text12, (560, 370))
            screen.blit(textt3, (605, 500))
            screen.blit(textt2, (235, 500))
            screen.blit(textt1, (75, 500))
            pygame.display.flip()

    if category == "animal":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Flip', True, (255, 255, 255))
        text2 = smallfont.render('Black-White', True, (255, 255, 255))
        text3 = smallfont.render('Blurred', True, (255, 255, 255))
        text4 = smallfont.render('Contours', True, (255, 255, 255))
        text5 = smallfont.render('Red', True, (255, 255, 255))
        text6 = smallfont.render('Green', True, (255, 255, 255))
        text7 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text8 = smallfont.render('High-Increasing-Contours', True, (255, 255, 255))
        text9 = smallfont.render('Dark', True, (255, 255, 255))
        text10 = smallfont.render('Light', True, (255, 255, 255))
        text11 = smallfont.render('Water-Color', True, (255, 255, 255))
        text12 = smallfont.render('Contrast', True, (255, 255, 255))
        text13 = smallfont.render('Higher-Contrast', True, (255, 255, 255))
        text14 = smallfont.render('Night', True, (255, 255, 255))
        text15 = smallfont.render('Black-White-Binary', True, (255, 255, 255))
        text16 = smallfont.render('Darkness', True, (255, 255, 255))
        color_light1 = (0, 0, 0)
        textt3 = smallfont.render('Choose & Exit', True, (255, 255, 255))
        textt2 = smallfont.render('Choose & Continue', True, (255, 255, 255))
        textt1 = smallfont.render('back', True, (255, 255, 255))

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
                    if 100 <= mouse[0] <= 100 + 55 and 22 <= mouse[1] <= 22 + 50:
                        filters_screen2(im, "flip")
                    if 230 <= mouse[0] <= 230 + 180 and 22 <= mouse[1] <= 22 + 50:
                        filters_screen2(im, "black-white")
                    if 490 <= mouse[0] <= 490 + 110 and 22 <= mouse[1] <= 22 + 50:
                        filters_screen2(im, "blurred")
                    if 670 <= mouse[0] <= 670 + 140 and 22 <= mouse[1] <= 22 + 50:
                        filters_screen2(im, "contours")
                    if 100 <= mouse[0] <= 100 + 60 and 122 <= mouse[1] <= 122 + 50:
                        filters_screen2(im, "red")
                    if 280 <= mouse[0] <= 280 + 90 and 122 <= mouse[1] <= 122 + 50:
                        filters_screen2(im, "green")
                    if 500 <= mouse[0] <= 500 + 300 and 122 <= mouse[1] <= 122 + 50:
                        filters_screen2(im, "increasing contours")
                    if 70 <= mouse[0] <= 70 + 375 and 222 <= mouse[1] <= 222 + 50:
                        filters_screen2(im, "high increasing contours")
                    if 515 <= mouse[0] <= 515 + 75 and 222 <= mouse[1] <= 222 + 50:
                        filters_screen2(im, "dark")
                    if 710 <= mouse[0] <= 710 + 75 and 222 <= mouse[1] <= 222 + 50:
                        filters_screen2(im, "light")
                    if 120 <= mouse[0] <= 120 + 175 and 322 <= mouse[1] <= 322 + 50:
                        filters_screen2(im, "water color")
                    if 350 <= mouse[0] <= 350 + 130 and 322 <= mouse[1] <= 322 + 50:
                        filters_screen2(im, "contrast")
                    if 540 <= mouse[0] <= 540 + 235 and 322 <= mouse[1] <= 322 + 50:
                        filters_screen2(im, "higher contrast")
                    if 80 <= mouse[0] <= 80 + 80 and 422 <= mouse[1] <= 422 + 50:
                        filters_screen2(im, "night")
                    if 280 <= mouse[0] <= 280 + 285 and 422 <= mouse[1] <= 422 + 50:
                        filters_screen2(im, "black-white binary")
                    if 660 <= mouse[0] <= 660 + 145 and 422 <= mouse[1] <= 422 + 50:
                        filters_screen2(im, "darkness")
                    if 595 <= mouse[0] <= 595 + 225 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("animal")
                        arr = [x, "save and exit"]
                        return arr
                    if 225 <= mouse[0] <= 225 + 310 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("animal")
                        arr = [x, "save and continue"]
                        return arr
                    if 65 <= mouse[0] <= 65 + 95 and 490 <= mouse[1] <= 490 + 50:
                        return "back"
            pygame.draw.rect(screen, color_light, [100, 22, 55, 50])
            pygame.draw.rect(screen, color_light, [230, 22, 180, 50])
            pygame.draw.rect(screen, color_light, [490, 22, 110, 50])
            pygame.draw.rect(screen, color_light, [670, 22, 140, 50])
            pygame.draw.rect(screen, color_light, [100, 122, 60, 50])
            pygame.draw.rect(screen, color_light, [280, 122, 90, 50])
            pygame.draw.rect(screen, color_light, [500, 122, 300, 50])
            pygame.draw.rect(screen, color_light, [70, 222, 375, 50])
            pygame.draw.rect(screen, color_light, [515, 222, 75, 50])
            pygame.draw.rect(screen, color_light, [710, 222, 75, 50])
            pygame.draw.rect(screen, color_light, [120, 322, 175, 50])
            pygame.draw.rect(screen, color_light, [350, 322, 130, 50])
            pygame.draw.rect(screen, color_light, [540, 322, 235, 50])
            pygame.draw.rect(screen, color_light, [80, 422, 80, 50])
            pygame.draw.rect(screen, color_light, [280, 422, 285, 50])
            pygame.draw.rect(screen, color_light, [660, 422, 145, 50])
            pygame.draw.rect(screen, color_light1, [595, 490, 225, 50])
            pygame.draw.rect(screen, color_light1, [225, 490, 310, 50])
            pygame.draw.rect(screen, color_light1, [65, 490, 95, 50])
            screen.blit(text1, (100, 32))
            screen.blit(text2, (230, 32))
            screen.blit(text3, (490, 32))
            screen.blit(text4, (670, 32))
            screen.blit(text5, (100, 132))
            screen.blit(text6, (280, 132))
            screen.blit(text7, (500, 132))
            screen.blit(text8, (70, 232))
            screen.blit(text9, (515, 232))
            screen.blit(text10, (710, 232))
            screen.blit(text11, (120, 332))
            screen.blit(text12, (350, 332))
            screen.blit(text13, (540, 332))
            screen.blit(text14, (80, 432))
            screen.blit(text15, (280, 432))
            screen.blit(text16, (660, 432))
            screen.blit(textt3, (605, 500))
            screen.blit(textt2, (235, 500))
            screen.blit(textt1, (75, 500))
            pygame.display.flip()

    if category == "food":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Black-White', True, (255, 255, 255))
        text2 = smallfont.render('Blurred', True, (255, 255, 255))
        text3 = smallfont.render('Red', True, (255, 255, 255))
        text4 = smallfont.render('Green', True, (255, 255, 255))
        text5 = smallfont.render('Black-White-Contours', True, (255, 255, 255))
        text6 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text7 = smallfont.render('Light', True, (255, 255, 255))
        text8 = smallfont.render('Water-Color', True, (255, 255, 255))
        text9 = smallfont.render('Contrast', True, (255, 255, 255))
        text10 = smallfont.render('High-Darkness', True, (255, 255, 255))
        color_light1 = (0, 0, 0)
        textt3 = smallfont.render('Choose & Exit', True, (255, 255, 255))
        textt2 = smallfont.render('Choose & Continue', True, (255, 255, 255))
        textt1 = smallfont.render('back', True, (255, 255, 255))

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
                    if 80 <= mouse[0] <= 80 + 180 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "black-white")
                    if 350 <= mouse[0] <= 350 + 110 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "blurred")
                    if 550 <= mouse[0] <= 550 + 60 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "red")
                    if 710 <= mouse[0] <= 710 + 90 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "green")
                    if 110 <= mouse[0] <= 110 + 325 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "black-white contours")
                    if 530 <= mouse[0] <= 530 + 300 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "increasing contours")
                    if 260 <= mouse[0] <= 260 + 75 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "light")
                    if 590 <= mouse[0] <= 590 + 175 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "water color")
                    if 230 <= mouse[0] <= 230 + 130 and 360 <= mouse[1] <= 360 + 50:
                        filters_screen2(im, "contrast")
                    if 565 <= mouse[0] <= 565 + 220 and 360 <= mouse[1] <= 360 + 50:
                        filters_screen2(im, "high darkness")
                    if 595 <= mouse[0] <= 595 + 225 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("food")
                        arr = [x, "save and exit"]
                        return arr
                    if 225 <= mouse[0] <= 225 + 310 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("food")
                        arr = [x, "save and continue"]
                        return arr
                    if 65 <= mouse[0] <= 65 + 95 and 490 <= mouse[1] <= 490 + 50:
                        return "back"
            pygame.draw.rect(screen, color_light, [80, 60, 180, 50])
            pygame.draw.rect(screen, color_light, [350, 60, 110, 50])
            pygame.draw.rect(screen, color_light, [550, 60, 60, 50])
            pygame.draw.rect(screen, color_light, [710, 60, 90, 50])
            pygame.draw.rect(screen, color_light, [110, 160, 325, 50])
            pygame.draw.rect(screen, color_light, [530, 160, 300, 50])
            pygame.draw.rect(screen, color_light, [260, 260, 75, 50])
            pygame.draw.rect(screen, color_light, [590, 260, 175, 50])
            pygame.draw.rect(screen, color_light, [230, 360, 130, 50])
            pygame.draw.rect(screen, color_light, [565, 360, 220, 50])
            pygame.draw.rect(screen, color_light1, [595, 490, 225, 50])
            pygame.draw.rect(screen, color_light1, [225, 490, 310, 50])
            pygame.draw.rect(screen, color_light1, [65, 490, 95, 50])
            screen.blit(text1, (80, 70))
            screen.blit(text2, (350, 70))
            screen.blit(text3, (550, 70))
            screen.blit(text4, (710, 70))
            screen.blit(text5, (110, 170))
            screen.blit(text6, (530, 170))
            screen.blit(text7, (260, 270))
            screen.blit(text8, (590, 270))
            screen.blit(text9, (230, 370))
            screen.blit(text10, (565, 370))
            screen.blit(textt3, (605, 500))
            screen.blit(textt2, (235, 500))
            screen.blit(textt1, (75, 500))
            pygame.display.flip()

    if category == "thing":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Flip', True, (255, 255, 255))
        text2 = smallfont.render('Black-White', True, (255, 255, 255))
        text3 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text4 = smallfont.render('Water-Color', True, (255, 255, 255))
        text5 = smallfont.render('Contrast', True, (255, 255, 255))
        text6 = smallfont.render('Darkness', True, (255, 255, 255))
        text7 = smallfont.render('Contours', True, (255, 255, 255))
        text8 = smallfont.render('Black-White-Binary', True, (255, 255, 255))
        color_light1 = (0, 0, 0)
        textt3 = smallfont.render('Choose & Exit', True, (255, 255, 255))
        textt2 = smallfont.render('Choose & Continue', True, (255, 255, 255))
        textt1 = smallfont.render('back', True, (255, 255, 255))

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
                    if 210 <= mouse[0] <= 210 + 55 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "flip")
                    if 540 <= mouse[0] <= 540 + 180 and 60 <= mouse[1] <= 60 + 50:
                        filters_screen2(im, "black-white")
                    if 80 <= mouse[0] <= 80 + 300 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "increasing contours")
                    if 540 <= mouse[0] <= 540 + 180 and 160 <= mouse[1] <= 160 + 50:
                        filters_screen2(im, "water color")
                    if 165 <= mouse[0] <= 165 + 130 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "contrast")
                    if 565 <= mouse[0] <= 565 + 145 and 260 <= mouse[1] <= 260 + 50:
                        filters_screen2(im, "darkness")
                    if 165 <= mouse[0] <= 165 + 135 and 360 <= mouse[1] <= 360 + 50:
                        filters_screen2(im, "contours")
                    if 490 <= mouse[0] <= 490 + 290 and 360 <= mouse[1] <= 360 + 50:
                        filters_screen2(im, "black-white binary")
                    if 595 <= mouse[0] <= 595 + 225 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("thing")
                        arr = [x, "save and exit"]
                        return arr
                    if 225 <= mouse[0] <= 225 + 310 and 490 <= mouse[1] <= 490 + 50:
                        x = filters_screen3("thing")
                        arr = [x, "save and continue"]
                        return arr
                    if 65 <= mouse[0] <= 65 + 95 and 490 <= mouse[1] <= 490 + 50:
                        return "back"
            pygame.draw.rect(screen, color_light, [210, 60, 55, 50])
            pygame.draw.rect(screen, color_light, [540, 60, 180, 50])
            pygame.draw.rect(screen, color_light, [80, 160, 300, 50])
            pygame.draw.rect(screen, color_light, [540, 160, 180, 50])
            pygame.draw.rect(screen, color_light, [165, 260, 130, 50])
            pygame.draw.rect(screen, color_light, [565, 260, 145, 50])
            pygame.draw.rect(screen, color_light, [165, 360, 135, 50])
            pygame.draw.rect(screen, color_light, [490, 360, 290, 50])
            pygame.draw.rect(screen, color_light1, [595, 490, 225, 50])
            pygame.draw.rect(screen, color_light1, [225, 490, 310, 50])
            pygame.draw.rect(screen, color_light1, [65, 490, 95, 50])
            screen.blit(text1, (210, 70))
            screen.blit(text2, (540, 70))
            screen.blit(text3, (80, 170))
            screen.blit(text4, (540, 170))
            screen.blit(text5, (165, 270))
            screen.blit(text6, (565, 270))
            screen.blit(text7, (165, 370))
            screen.blit(text8, (490, 370))
            screen.blit(textt3, (605, 500))
            screen.blit(textt2, (235, 500))
            screen.blit(textt1, (75, 500))
            pygame.display.flip()


# shows the filters
def filters_screen2(image, subject):
    # the window that opens with which the user sees each of the filters
    window = tk.Tk()
    window.title("Image Design")
    window.geometry("800x700")
    im = Image.open(image)
    enh = ImageEnhance.Contrast(im) # the contrast of the image
    width, height = im.size
    data1 = im.getdata()   # turns the value of each pixel into an array of numbers where each pixel gets 3 numbers that represent the colors red, green and blue
    R = []
    G = []
    for i in data1:
        R.append((i[0], 0, 0))   # the first value from which the pixel is built is red
        G.append((0, i[1], 0))   # the second value from which the pixel is built is green
    imgR = Image.new(mode="RGB", size=(width, height))
    imgG = Image.new(mode="RGB", size=(width, height))
    imgR.putdata(R)
    imgG.putdata(G)
    if subject == "flip":
        im_data = np.array(im)
        img_flipped_data = np.flip(im_data, axis=1)
        img_flipped = ImageTk.PhotoImage(Image.fromarray(img_flipped_data))
        panel = tk.Label(window, background="white", image=img_flipped)
        panel.pack()
    if subject == "black-white":
        im1 = ImageTk.PhotoImage(im.convert(mode='L'))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "black-white contours":
        im1 = ImageTk.PhotoImage((im.convert(mode='L')).filter(ImageFilter.CONTOUR))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "increasing contours":
        im1 = ImageTk.PhotoImage(im.filter(ImageFilter.EDGE_ENHANCE))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "light":
        im1 = ImageTk.PhotoImage(im.filter(ImageFilter.MaxFilter(size=3)))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "water color":
        im1 = ImageTk.PhotoImage(im.filter(ImageFilter.ModeFilter(size=6)))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "contrast":
        im1 = ImageTk.PhotoImage(enh.enhance(1.5))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "darkness":
        im1 = ImageTk.PhotoImage(enh.enhance(0.6))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "contours":
        im1 = ImageTk.PhotoImage(im.filter(ImageFilter.CONTOUR))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "red":
        im1 = ImageTk.PhotoImage(imgR)
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "night":
        im1 = ImageTk.PhotoImage(ImageChops.invert(im))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "dark":
        im1 = ImageTk.PhotoImage(im.filter(ImageFilter.MinFilter(size=3)))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "black-white binary":
        bin_im = get_binary_image(im, 100)
        im1 = ImageTk.PhotoImage(bin_im)
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "high increasing contours":
        im1 = ImageTk.PhotoImage(im.filter(ImageFilter.UnsharpMask( radius=3, percent=250, threshold=4)))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "high darkness":
        im1 = ImageTk.PhotoImage(enh.enhance(0.3))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "blurred":
        im1 = ImageTk.PhotoImage(im.filter(ImageFilter.BLUR))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "green":
        im1 = ImageTk.PhotoImage(imgG)
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    if subject == "higher contrast":
        im1 = ImageTk.PhotoImage(enh.enhance(1.8))
        panel = tk.Label(window, background="white", image=im1)
        panel.pack()
    window.mainloop()


# shows screen with buttons of the filters by categories and the user need choose a filter
def filters_screen3(category):
    # the graphics of the screen
    window_width = 900
    window_height = 600
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

    if category == "person":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Flip', True, (255, 255, 255))
        text2 = smallfont.render('Black-White', True, (255, 255, 255))
        text3 = smallfont.render('Black-White-Contours', True, (255, 255, 255))
        text4 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text5 = smallfont.render('Light', True, (255, 255, 255))
        text6 = smallfont.render('Water-Color', True, (255, 255, 255))
        text7 = smallfont.render('Contrast', True, (255, 255, 255))
        text8 = smallfont.render('Darkness', True, (255, 255, 255))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 210 <= mouse[0] <= 210 + 55 and 60 <= mouse[1] <= 60 + 50:
                        return "flip"
                    if 540 <= mouse[0] <= 540 + 180 and 60 <= mouse[1] <= 60 + 50:
                        return "black-white"
                    if 80 <= mouse[0] <= 80 + 325 and 160 <= mouse[1] <= 160 + 50:
                        return "black-white contours"
                    if 490 <= mouse[0] <= 490 + 300 and 160 <= mouse[1] <= 160 + 50:
                        return "increasing contours"
                    if 200 <= mouse[0] <= 200 + 75 and 260 <= mouse[1] <= 260 + 50:
                        return "light"
                    if 545 <= mouse[0] <= 545 + 180 and 260 <= mouse[1] <= 260 + 50:
                        return "water color"
                    if 170 <= mouse[0] <= 170 + 130 and 360 <= mouse[1] <= 360 + 50:
                        return "contrast"
                    if 560 <= mouse[0] <= 560 + 145 and 360 <= mouse[1] <= 360 + 50:
                        return "darkness"
            pygame.draw.rect(screen, color_light, [210, 60, 55, 50])
            pygame.draw.rect(screen, color_light, [540, 60, 180, 50])
            pygame.draw.rect(screen, color_light, [80, 160, 325, 50])
            pygame.draw.rect(screen, color_light, [490, 160, 300, 50])
            pygame.draw.rect(screen, color_light, [200, 260, 75, 50])
            pygame.draw.rect(screen, color_light, [545, 260, 180, 50])
            pygame.draw.rect(screen, color_light, [170, 360, 130, 50])
            pygame.draw.rect(screen, color_light, [560, 360, 145, 50])
            screen.blit(text1, (210, 70))
            screen.blit(text2, (540, 70))
            screen.blit(text3, (80, 170))
            screen.blit(text4, (490, 170))
            screen.blit(text5, (200, 270))
            screen.blit(text6, (545, 270))
            screen.blit(text7, (170, 370))
            screen.blit(text8, (560, 370))
            pygame.display.flip()

    if category == "vehicle":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Flip', True, (255, 255, 255))
        text2 = smallfont.render('Black-White', True, (255, 255, 255))
        text3 = smallfont.render('Contours', True, (255, 255, 255))
        text4 = smallfont.render('Red', True, (255, 255, 255))
        text5 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text6 = smallfont.render('Night', True, (255, 255, 255))
        text7 = smallfont.render('Dark', True, (255, 255, 255))
        text8 = smallfont.render('Water-Color', True, (255, 255, 255))
        text9 = smallfont.render('Contrast', True, (255, 255, 255))
        text10 = smallfont.render('Black-White-Binary', True, (255, 255, 255))
        text11 = smallfont.render('High-Increasing-Contours', True, (255, 255, 255))
        text12 = smallfont.render('High-Darkness', True, (255, 255, 255))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 55 and 60 <= mouse[1] <= 60 + 50:
                        return "flip"
                    if 250 <= mouse[0] <= 250 + 180 and 60 <= mouse[1] <= 60 + 50:
                        return "black-white"
                    if 520 <= mouse[0] <= 520 + 135 and 60 <= mouse[1] <= 60 + 50:
                        return "contours"
                    if 750 <= mouse[0] <= 750 + 60 and 60 <= mouse[1] <= 60 + 50:
                        return "red"
                    if 115 <= mouse[0] <= 115 + 300 and 160 <= mouse[1] <= 160 + 50:
                        return "increasing contours"
                    if 555 <= mouse[0] <= 555 + 80 and 160 <= mouse[1] <= 160 + 50:
                        return "night"
                    if 745 <= mouse[0] <= 745 + 75 and 160 <= mouse[1] <= 160 + 50:
                        return "dark"
                    if 100 <= mouse[0] <= 100 + 180 and 260 <= mouse[1] <= 260 + 50:
                        return "water color"
                    if 350 <= mouse[0] <= 350 + 130 and 260 <= mouse[1] <= 260 + 50:
                        return "contrast"
                    if 540 <= mouse[0] <= 540 + 290 and 260 <= mouse[1] <= 260 + 50:
                        return "black-white binary"
                    if 80 <= mouse[0] <= 80 + 380 and 360 <= mouse[1] <= 360 + 50:
                        return "high increasing contours"
                    if 560 <= mouse[0] <= 560 + 220 and 360 <= mouse[1] <= 360 + 50:
                        return "high darkness"
            pygame.draw.rect(screen, color_light, [100, 60, 55, 50])
            pygame.draw.rect(screen, color_light, [250, 60, 180, 50])
            pygame.draw.rect(screen, color_light, [520, 60, 135, 50])
            pygame.draw.rect(screen, color_light, [750, 60, 60, 50])
            pygame.draw.rect(screen, color_light, [115, 160, 300, 50])
            pygame.draw.rect(screen, color_light, [555, 160, 80, 50])
            pygame.draw.rect(screen, color_light, [745, 160, 75, 50])
            pygame.draw.rect(screen, color_light, [100, 260, 180, 50])
            pygame.draw.rect(screen, color_light, [350, 260, 130, 50])
            pygame.draw.rect(screen, color_light, [540, 260, 290, 50])
            pygame.draw.rect(screen, color_light, [80, 360, 380, 50])
            pygame.draw.rect(screen, color_light, [560, 360, 220, 50])
            screen.blit(text1, (100, 70))
            screen.blit(text2, (250, 70))
            screen.blit(text3, (520, 70))
            screen.blit(text4, (750, 70))
            screen.blit(text5, (115, 170))
            screen.blit(text6, (555, 170))
            screen.blit(text7, (745, 170))
            screen.blit(text8, (100, 270))
            screen.blit(text9, (350, 270))
            screen.blit(text10, (540, 270))
            screen.blit(text11, (80, 370))
            screen.blit(text12, (560, 370))
            pygame.display.flip()

    if category == "animal":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Flip', True, (255, 255, 255))
        text2 = smallfont.render('Black-White', True, (255, 255, 255))
        text3 = smallfont.render('Blurred', True, (255, 255, 255))
        text4 = smallfont.render('Contours', True, (255, 255, 255))
        text5 = smallfont.render('Red', True, (255, 255, 255))
        text6 = smallfont.render('Green', True, (255, 255, 255))
        text7 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text8 = smallfont.render('High-Increasing-Contours', True, (255, 255, 255))
        text9 = smallfont.render('Dark', True, (255, 255, 255))
        text10 = smallfont.render('Light', True, (255, 255, 255))
        text11 = smallfont.render('Water-Color', True, (255, 255, 255))
        text12 = smallfont.render('Contrast', True, (255, 255, 255))
        text13 = smallfont.render('Higher-Contrast', True, (255, 255, 255))
        text14 = smallfont.render('Night', True, (255, 255, 255))
        text15 = smallfont.render('Black-White-Binary', True, (255, 255, 255))
        text16 = smallfont.render('Darkness', True, (255, 255, 255))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 55 and 22 <= mouse[1] <= 22 + 50:
                        return "flip"
                    if 230 <= mouse[0] <= 230 + 180 and 22 <= mouse[1] <= 22 + 50:
                        return "black-white"
                    if 490 <= mouse[0] <= 490 + 110 and 22 <= mouse[1] <= 22 + 50:
                        return "blurred"
                    if 670 <= mouse[0] <= 670 + 140 and 22 <= mouse[1] <= 22 + 50:
                        return "contours"
                    if 100 <= mouse[0] <= 100 + 60 and 122 <= mouse[1] <= 122 + 50:
                        return "red"
                    if 280 <= mouse[0] <= 280 + 90 and 122 <= mouse[1] <= 122 + 50:
                        return "green"
                    if 500 <= mouse[0] <= 500 + 300 and 122 <= mouse[1] <= 122 + 50:
                        return "increasing contours"
                    if 70 <= mouse[0] <= 70 + 375 and 222 <= mouse[1] <= 222 + 50:
                        return "high increasing contours"
                    if 515 <= mouse[0] <= 515 + 75 and 222 <= mouse[1] <= 222 + 50:
                        return "dark"
                    if 710 <= mouse[0] <= 710 + 75 and 222 <= mouse[1] <= 222 + 50:
                        return "light"
                    if 120 <= mouse[0] <= 120 + 175 and 322 <= mouse[1] <= 322 + 50:
                        return "water color"
                    if 350 <= mouse[0] <= 350 + 130 and 322 <= mouse[1] <= 322 + 50:
                        return "contrast"
                    if 540 <= mouse[0] <= 540 + 235 and 322 <= mouse[1] <= 322 + 50:
                        return "higher contrast"
                    if 80 <= mouse[0] <= 80 + 80 and 422 <= mouse[1] <= 422 + 50:
                        return "night"
                    if 280 <= mouse[0] <= 280 + 285 and 422 <= mouse[1] <= 422 + 50:
                        return "black-white binary"
                    if 660 <= mouse[0] <= 660 + 145 and 422 <= mouse[1] <= 422 + 50:
                        return "darkness"
            pygame.draw.rect(screen, color_light, [100, 22, 55, 50])
            pygame.draw.rect(screen, color_light, [230, 22, 180, 50])
            pygame.draw.rect(screen, color_light, [490, 22, 110, 50])
            pygame.draw.rect(screen, color_light, [670, 22, 140, 50])
            pygame.draw.rect(screen, color_light, [100, 122, 60, 50])
            pygame.draw.rect(screen, color_light, [280, 122, 90, 50])
            pygame.draw.rect(screen, color_light, [500, 122, 300, 50])
            pygame.draw.rect(screen, color_light, [70, 222, 375, 50])
            pygame.draw.rect(screen, color_light, [515, 222, 75, 50])
            pygame.draw.rect(screen, color_light, [710, 222, 75, 50])
            pygame.draw.rect(screen, color_light, [120, 322, 175, 50])
            pygame.draw.rect(screen, color_light, [350, 322, 130, 50])
            pygame.draw.rect(screen, color_light, [540, 322, 235, 50])
            pygame.draw.rect(screen, color_light, [80, 422, 80, 50])
            pygame.draw.rect(screen, color_light, [280, 422, 285, 50])
            pygame.draw.rect(screen, color_light, [660, 422, 145, 50])
            screen.blit(text1, (100, 32))
            screen.blit(text2, (230, 32))
            screen.blit(text3, (490, 32))
            screen.blit(text4, (670, 32))
            screen.blit(text5, (100, 132))
            screen.blit(text6, (280, 132))
            screen.blit(text7, (500, 132))
            screen.blit(text8, (70, 232))
            screen.blit(text9, (515, 232))
            screen.blit(text10, (710, 232))
            screen.blit(text11, (120, 332))
            screen.blit(text12, (350, 332))
            screen.blit(text13, (540, 332))
            screen.blit(text14, (80, 432))
            screen.blit(text15, (280, 432))
            screen.blit(text16, (660, 432))
            pygame.display.flip()

    if category == "food":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Black-White', True, (255, 255, 255))
        text2 = smallfont.render('Blurred', True, (255, 255, 255))
        text3 = smallfont.render('Red', True, (255, 255, 255))
        text4 = smallfont.render('Green', True, (255, 255, 255))
        text5 = smallfont.render('Black-White-Contours', True, (255, 255, 255))
        text6 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text7 = smallfont.render('Light', True, (255, 255, 255))
        text8 = smallfont.render('Water-Color', True, (255, 255, 255))
        text9 = smallfont.render('Contrast', True, (255, 255, 255))
        text10 = smallfont.render('High-Darkness', True, (255, 255, 255))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 80 <= mouse[0] <= 80 + 180 and 60 <= mouse[1] <= 60 + 50:
                        return "black-white"
                    if 350 <= mouse[0] <= 350 + 110 and 60 <= mouse[1] <= 60 + 50:
                        return "blurred"
                    if 550 <= mouse[0] <= 550 + 60 and 60 <= mouse[1] <= 60 + 50:
                        return "red"
                    if 710 <= mouse[0] <= 710 + 90 and 60 <= mouse[1] <= 60 + 50:
                        return "green"
                    if 110 <= mouse[0] <= 110 + 325 and 160 <= mouse[1] <= 160 + 50:
                        return "black-white contours"
                    if 530 <= mouse[0] <= 530 + 300 and 160 <= mouse[1] <= 160 + 50:
                        return "increasing contours"
                    if 260 <= mouse[0] <= 260 + 75 and 260 <= mouse[1] <= 260 + 50:
                        return "light"
                    if 590 <= mouse[0] <= 590 + 175 and 260 <= mouse[1] <= 260 + 50:
                        return "water color"
                    if 230 <= mouse[0] <= 230 + 130 and 360 <= mouse[1] <= 360 + 50:
                        return "contrast"
                    if 565 <= mouse[0] <= 565 + 220 and 360 <= mouse[1] <= 360 + 50:
                        return "high darkness"
            pygame.draw.rect(screen, color_light, [80, 60, 180, 50])
            pygame.draw.rect(screen, color_light, [350, 60, 110, 50])
            pygame.draw.rect(screen, color_light, [550, 60, 60, 50])
            pygame.draw.rect(screen, color_light, [710, 60, 90, 50])
            pygame.draw.rect(screen, color_light, [110, 160, 325, 50])
            pygame.draw.rect(screen, color_light, [530, 160, 300, 50])
            pygame.draw.rect(screen, color_light, [260, 260, 75, 50])
            pygame.draw.rect(screen, color_light, [590, 260, 175, 50])
            pygame.draw.rect(screen, color_light, [230, 360, 130, 50])
            pygame.draw.rect(screen, color_light, [565, 360, 220, 50])
            screen.blit(text1, (80, 70))
            screen.blit(text2, (350, 70))
            screen.blit(text3, (550, 70))
            screen.blit(text4, (710, 70))
            screen.blit(text5, (110, 170))
            screen.blit(text6, (530, 170))
            screen.blit(text7, (260, 270))
            screen.blit(text8, (590, 270))
            screen.blit(text9, (230, 370))
            screen.blit(text10, (565, 370))
            pygame.display.flip()

    if category == "thing":

        color_light = (44, 118, 131)
        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Flip', True, (255, 255, 255))
        text2 = smallfont.render('Black-White', True, (255, 255, 255))
        text3 = smallfont.render('Increasing-Contours', True, (255, 255, 255))
        text4 = smallfont.render('Water-Color', True, (255, 255, 255))
        text5 = smallfont.render('Contrast', True, (255, 255, 255))
        text6 = smallfont.render('Darkness', True, (255, 255, 255))
        text7 = smallfont.render('Contours', True, (255, 255, 255))
        text8 = smallfont.render('Black-White-Binary', True, (255, 255, 255))
        # the buttons on the screen
        pygame.display.flip()

        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 210 <= mouse[0] <= 210 + 55 and 60 <= mouse[1] <= 60 + 50:
                        return "flip"
                    if 540 <= mouse[0] <= 540 + 180 and 60 <= mouse[1] <= 60 + 50:
                        return "black-white"
                    if 80 <= mouse[0] <= 80 + 300 and 160 <= mouse[1] <= 160 + 50:
                        return "increasing contours"
                    if 540 <= mouse[0] <= 540 + 180 and 160 <= mouse[1] <= 160 + 50:
                        return "water color"
                    if 165 <= mouse[0] <= 165 + 130 and 260 <= mouse[1] <= 260 + 50:
                        return "contrast"
                    if 565 <= mouse[0] <= 565 + 145 and 260 <= mouse[1] <= 260 + 50:
                        return "darkness"
                    if 165 <= mouse[0] <= 165 + 135 and 360 <= mouse[1] <= 360 + 50:
                        return "contours"
                    if 490 <= mouse[0] <= 490 + 290 and 360 <= mouse[1] <= 360 + 50:
                        return "black-white binary"
            pygame.draw.rect(screen, color_light, [210, 60, 55, 50])
            pygame.draw.rect(screen, color_light, [540, 60, 180, 50])
            pygame.draw.rect(screen, color_light, [80, 160, 300, 50])
            pygame.draw.rect(screen, color_light, [540, 160, 180, 50])
            pygame.draw.rect(screen, color_light, [165, 260, 130, 50])
            pygame.draw.rect(screen, color_light, [565, 260, 145, 50])
            pygame.draw.rect(screen, color_light, [165, 360, 135, 50])
            pygame.draw.rect(screen, color_light, [490, 360, 290, 50])
            screen.blit(text1, (210, 70))
            screen.blit(text2, (540, 70))
            screen.blit(text3, (80, 170))
            screen.blit(text4, (540, 170))
            screen.blit(text5, (165, 270))
            screen.blit(text6, (565, 270))
            screen.blit(text7, (165, 370))
            screen.blit(text8, (490, 370))
            pygame.display.flip()
