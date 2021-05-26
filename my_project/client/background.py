import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import pygame


# removes the background in the image and switches to another background
def change_backrounds(img, bg):
    img2 = img
    src = cv2.imread(bg, cv2.IMREAD_UNCHANGED)
    width = img2.shape[1]
    height = img2.shape[0]
    dsize = (width, height)
    output = cv2.resize(src, dsize) # the size of the new image is the same as the size of the original image
    cv2.imwrite(bg, output)
    img1 = cv2.imread(bg)
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]

    # creates a mask of the image and creates its inverse mask also
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # black-out the area of the image in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # takes only region of the image
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # puts the image in ROI and modify the main image
    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst
    return cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)


# shows screen with buttons of the backgrounds by categories
def backgrounds_screen1(im, category):
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

    if category == "person":

        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Beach', True, (255, 255, 255))
        text2 = smallfont.render('Lawn', True, (255, 255, 255))
        text3 = smallfont.render('Snow', True, (0, 0, 0))
        text4 = smallfont.render('Sky', True, (255, 255, 255))
        text5 = smallfont.render('Road', True, (255, 255, 255))
        text6 = smallfont.render('Park', True, (255, 255, 255))
        text7 = smallfont.render('Pathway', True, (0, 0, 0))
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
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 90 <= mouse[0] <= 90 + 120 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "beach")
                    if 290 <= mouse[0] <= 290 + 120 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "lawn")
                    if 490 <= mouse[0] <= 490 + 120 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "snow")
                    if 90 <= mouse[0] <= 90 + 120 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "sky")
                    if 290 <= mouse[0] <= 290 + 120 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "road")
                    if 490 <= mouse[0] <= 490 + 120 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "park")
                    if 280 <= mouse[0] <= 280 + 140 and 330 <= mouse[1] <= 330 + 50:
                        backgrounds_screen2(im, "pathway")
                    if 440 <= mouse[0] <= 440 + 230 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("person")
                        arr = [x, "save and exit"]
                        return arr
                    if 130 <= mouse[0] <= 130 + 300 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("person")
                        arr = [x, "save and continue"]
                        return arr
                    if 30 <= mouse[0] <= 30 + 90 and 420 <= mouse[1] <= 420 + 50:
                        return "back"
            pygame.draw.rect(screen, (66, 216, 253), [90, 90, 120, 50])
            pygame.draw.rect(screen, (73, 173, 14), [290, 90, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [490, 90, 120, 50])
            pygame.draw.rect(screen, (104, 38, 102), [90, 210, 120, 50])
            pygame.draw.rect(screen, (66, 77, 79), [290, 210, 120, 50])
            pygame.draw.rect(screen, (103, 236, 23), [490, 210, 120, 50])
            pygame.draw.rect(screen, (255, 231, 206), [280, 330, 140, 50])
            pygame.draw.rect(screen, color_light1, [440, 420, 230, 50])
            pygame.draw.rect(screen, color_light1, [130, 420, 300, 50])
            pygame.draw.rect(screen, color_light1, [30, 420, 90, 50])
            screen.blit(text1, (105, 100))
            screen.blit(text2, (310, 100))
            screen.blit(text3, (510, 100))
            screen.blit(text4, (117, 220))
            screen.blit(text5, (312, 220))
            screen.blit(text6, (517, 220))
            screen.blit(text7, (290, 340))
            screen.blit(textt3, (450, 430))
            screen.blit(textt2, (140, 430))
            screen.blit(textt1, (40, 430))
            pygame.display.flip()

    if category == "vehicle":

        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Garage 1', True, (255, 255, 255))
        text2 = smallfont.render('Garage 2', True, (255, 255, 255))
        text3 = smallfont.render('Outside Parking 1', True, (255, 255, 255))
        text4 = smallfont.render('Outside Parking 2', True, (255, 255, 255))
        text5 = smallfont.render('Underground Parking', True, (255, 255, 255))
        text6 = smallfont.render('Pathway', True, (0, 0, 0))
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
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 90 <= mouse[0] <= 90 + 150 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "garage1")
                    if 460 <= mouse[0] <= 460 + 150 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "garage2")
                    if 40 <= mouse[0] <= 40 + 290 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "parking1")
                    if 370 <= mouse[0] <= 370 + 290 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "parking2")
                    if 70 <= mouse[0] <= 70 + 340 and 330 <= mouse[1] <= 330 + 50:
                        backgrounds_screen2(im, "parking3")
                    if 490 <= mouse[0] <= 490 + 140 and 330 <= mouse[1] <= 330 + 50:
                        backgrounds_screen2(im, "pathway")
                    if 440 <= mouse[0] <= 440 + 230 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("vehicle")
                        arr = [x, "save and exit"]
                        return arr
                    if 130 <= mouse[0] <= 130 + 300 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("vehicle")
                        arr = [x, "save and continue"]
                        return arr
                    if 30 <= mouse[0] <= 30 + 90 and 420 <= mouse[1] <= 420 + 50:
                        return "back"
            pygame.draw.rect(screen, (139, 139, 139), [90, 90, 150, 50])
            pygame.draw.rect(screen, (90, 90, 90), [460, 90, 150, 50])
            pygame.draw.rect(screen, (191, 191, 191), [40, 210, 290, 50])
            pygame.draw.rect(screen, (112, 112, 112), [370, 210, 290, 50])
            pygame.draw.rect(screen, (141, 141, 141), [70, 330, 340, 50])
            pygame.draw.rect(screen, (255, 231, 206), [490, 330, 140, 50])
            pygame.draw.rect(screen, color_light1, [440, 420, 230, 50])
            pygame.draw.rect(screen, color_light1, [130, 420, 300, 50])
            pygame.draw.rect(screen, color_light1, [30, 420, 90, 50])
            screen.blit(text1, (100, 100))
            screen.blit(text2, (468, 100))
            screen.blit(text3, (50, 220))
            screen.blit(text4, (380, 220))
            screen.blit(text5, (80, 340))
            screen.blit(text6, (500, 340))
            screen.blit(textt3, (450, 430))
            screen.blit(textt2, (140, 430))
            screen.blit(textt1, (40, 430))
            pygame.display.flip()

    if category == "animal":

        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Desert', True, (255, 255, 255))
        text2 = smallfont.render('Forest', True, (255, 255, 255))
        text3 = smallfont.render('Lawn', True, (255, 255, 255))
        text4 = smallfont.render('Snow', True, (0, 0, 0))
        text5 = smallfont.render('Sky', True, (255, 255, 255))
        text6 = smallfont.render('Road', True, (255, 255, 255))
        text7 = smallfont.render('Wall', True, (0, 0, 0))
        text8 = smallfont.render('Pathway', True, (0, 0, 0))
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
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 60 <= mouse[0] <= 60 + 120 and 140 <= mouse[1] <= 140 + 50:
                        backgrounds_screen2(im, "desert")
                    if 220 <= mouse[0] <= 220 + 120 and 140 <= mouse[1] <= 140 + 50:
                        backgrounds_screen2(im, "forest")
                    if 370 <= mouse[0] <= 370 + 120 and 140 <= mouse[1] <= 140 + 50:
                        backgrounds_screen2(im, "lawn")
                    if 525 <= mouse[0] <= 525 + 120 and 140 <= mouse[1] <= 140 + 50:
                        backgrounds_screen2(im, "snow")
                    if 60 <= mouse[0] <= 60 + 120 and 290 <= mouse[1] <= 290 + 50:
                        backgrounds_screen2(im, "sky")
                    if 220 <= mouse[0] <= 220 + 120 and 290 <= mouse[1] <= 290 + 50:
                        backgrounds_screen2(im, "road")
                    if 370 <= mouse[0] <= 370 + 120 and 290 <= mouse[1] <= 290 + 50:
                        backgrounds_screen2(im, "wall")
                    if 505 <= mouse[0] <= 505 + 140 and 290 <= mouse[1] <= 290 + 50:
                        backgrounds_screen2(im, "pathway")
                    if 440 <= mouse[0] <= 440 + 230 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("animal")
                        arr = [x, "save and exit"]
                        return arr
                    if 130 <= mouse[0] <= 130 + 300 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("animal")
                        arr = [x, "save and continue"]
                        return arr
                    if 30 <= mouse[0] <= 30 + 90 and 420 <= mouse[1] <= 420 + 50:
                        return "back"
            pygame.draw.rect(screen, (140, 70, 0), [60, 140, 120, 50])
            pygame.draw.rect(screen, (50, 156, 10), [220, 140, 120, 50])
            pygame.draw.rect(screen, (73, 173, 14), [370, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [525, 140, 120, 50])
            pygame.draw.rect(screen, (104, 38, 102), [60, 290, 120, 50])
            pygame.draw.rect(screen, (66, 77, 79), [220, 290, 120, 50])
            pygame.draw.rect(screen, (197, 197, 197), [370, 290, 120, 50])
            pygame.draw.rect(screen, (255, 231, 206), [505, 290, 140, 50])
            pygame.draw.rect(screen, color_light1, [440, 420, 230, 50])
            pygame.draw.rect(screen, color_light1, [130, 420, 300, 50])
            pygame.draw.rect(screen, color_light1, [30, 420, 90, 50])
            screen.blit(text1, (70, 150))
            screen.blit(text2, (235, 150))
            screen.blit(text3, (390, 150))
            screen.blit(text4, (545, 150))
            screen.blit(text5, (90, 300))
            screen.blit(text6, (245, 300))
            screen.blit(text7, (400, 300))
            screen.blit(text8, (512, 300))
            screen.blit(textt3, (450, 430))
            screen.blit(textt2, (140, 430))
            screen.blit(textt1, (40, 430))
            pygame.display.flip()

    if category == "food":

        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('brown wood', True, (255, 255, 255))
        text2 = smallfont.render('white wood', True, (0, 0, 0))
        text3 = smallfont.render('bright wood', True, (255, 255, 255))
        text4 = smallfont.render('gray wood', True, (255, 255, 255))
        text5 = smallfont.render('light blue wood', True, (255, 255, 255))
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
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 90 <= mouse[0] <= 90 + 195 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "brown wood")
                    if 440 <= mouse[0] <= 440 + 185 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "white wood")
                    if 90 <= mouse[0] <= 90 + 195 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "bright wood")
                    if 440 <= mouse[0] <= 440 + 185 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "gray wood")
                    if 240 <= mouse[0] <= 240 + 250 and 330 <= mouse[1] <= 330 + 50:
                        backgrounds_screen2(im, "light blue wood")
                    if 440 <= mouse[0] <= 440 + 230 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("food")
                        arr = [x, "save and exit"]
                        return arr
                    if 130 <= mouse[0] <= 130 + 300 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("food")
                        arr = [x, "save and continue"]
                        return arr
                    if 30 <= mouse[0] <= 30 + 90 and 420 <= mouse[1] <= 420 + 50:
                        return "back"
            pygame.draw.rect(screen, (89, 45, 0), [90, 90, 195, 50])
            pygame.draw.rect(screen, (255, 255, 255), [440, 90, 185, 50])
            pygame.draw.rect(screen, (189, 136, 104), [90, 210, 195, 50])
            pygame.draw.rect(screen, (160, 177, 188), [440, 210, 185, 50])
            pygame.draw.rect(screen, (121, 181, 189), [240, 330, 250, 50])
            pygame.draw.rect(screen, color_light1, [440, 420, 230, 50])
            pygame.draw.rect(screen, color_light1, [130, 420, 300, 50])
            pygame.draw.rect(screen, color_light1, [30, 420, 90, 50])
            screen.blit(text1, (100, 100))
            screen.blit(text2, (450, 100))
            screen.blit(text3, (100, 220))
            screen.blit(text4, (460, 220))
            screen.blit(text5, (255, 340))
            screen.blit(textt3, (450, 430))
            screen.blit(textt2, (140, 430))
            screen.blit(textt1, (40, 430))
            pygame.display.flip()

    if category == "thing":

        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Forest', True, (255, 255, 255))
        text2 = smallfont.render('Lawn', True, (255, 255, 255))
        text3 = smallfont.render('Sky', True, (255, 255, 255))
        text4 = smallfont.render('Wall', True, (0, 0, 0))
        text5 = smallfont.render('White-Wood', True, (0, 0, 0))
        text6 = smallfont.render('Brown-Wood', True, (255, 255, 255))
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
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 130 <= mouse[0] <= 130 + 110 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "forest")
                    if 490 <= mouse[0] <= 490 + 100 and 90 <= mouse[1] <= 90 + 50:
                        backgrounds_screen2(im, "lawn")
                    if 150 <= mouse[0] <= 150 + 80 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "sky")
                    if 500 <= mouse[0] <= 500 + 80 and 210 <= mouse[1] <= 210 + 50:
                        backgrounds_screen2(im, "wall")
                    if 85 <= mouse[0] <= 85 + 200 and 330 <= mouse[1] <= 330 + 50:
                        backgrounds_screen2(im, "white wood")
                    if 435 <= mouse[0] <= 435 + 210 and 330 <= mouse[1] <= 330 + 50:
                        backgrounds_screen2(im, "brown wood")
                    if 440 <= mouse[0] <= 440 + 230 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("thing")
                        arr = [x, "save and exit"]
                        return arr
                    if 130 <= mouse[0] <= 130 + 300 and 420 <= mouse[1] <= 420 + 50:
                        x = backgrounds_screen3("thing")
                        arr = [x, "save and continue"]
                        return arr
                    if 30 <= mouse[0] <= 30 + 90 and 420 <= mouse[1] <= 420 + 50:
                        return "back"
            pygame.draw.rect(screen, (50, 156, 10), [130, 90, 110, 50])
            pygame.draw.rect(screen, (73, 173, 14), [490, 90, 100, 50])
            pygame.draw.rect(screen, (104, 38, 102), [150, 210, 80, 50])
            pygame.draw.rect(screen, (197, 197, 197), [500, 210, 80, 50])
            pygame.draw.rect(screen, (255, 255, 255), [85, 330, 200, 50])
            pygame.draw.rect(screen, (89, 45, 0), [435, 330, 210, 50])
            pygame.draw.rect(screen, color_light1, [440, 420, 230, 50])
            pygame.draw.rect(screen, color_light1, [130, 420, 300, 50])
            pygame.draw.rect(screen, color_light1, [30, 420, 90, 50])
            screen.blit(text1, (140, 100))
            screen.blit(text2, (500, 100))
            screen.blit(text3, (160, 220))
            screen.blit(text4, (510, 220))
            screen.blit(text5, (95, 340))
            screen.blit(text6, (445, 340))
            screen.blit(textt3, (450, 430))
            screen.blit(textt2, (140, 430))
            screen.blit(textt1, (40, 430))
            pygame.display.flip()


# shows the backgrounds
def backgrounds_screen2(img, subject):
    window = tk.Tk()
    window.title("Image Design")
    window.geometry("800x700")
    if subject == "beach":
        im1 = Image.fromarray(change_backrounds(img, 'images/beach.png'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "lawn":
        im1 = Image.fromarray(change_backrounds(img, 'images/lawn.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "snow":
        im1 = Image.fromarray(change_backrounds(img, 'images/snow.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "sky":
        im1 = Image.fromarray(change_backrounds(img, 'images/sky.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "road":
        im1 = Image.fromarray(change_backrounds(img, 'images/road.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "park":
        im1 = Image.fromarray(change_backrounds(img, 'images/park.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "pathway":
        im1 = Image.fromarray(change_backrounds(img, 'images/pathway.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "garage1":
        im1 = Image.fromarray(change_backrounds(img, 'images/garage_1.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "garage2":
        im1 = Image.fromarray(change_backrounds(img, 'images/garage_2.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "parking1":
        im1 = Image.fromarray(change_backrounds(img, 'images/parking_1.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "parking2":
        im1 = Image.fromarray(change_backrounds(img, 'images/parking_2.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "parking3":
        im1 = Image.fromarray(change_backrounds(img, 'images/parking_3.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "desert":
        im1 = Image.fromarray(change_backrounds(img, 'images/desert.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "forest":
        im1 = Image.fromarray(change_backrounds(img, 'images/forest.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "wall":
        im1 = Image.fromarray(change_backrounds(img, 'images/wall.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "brown wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/brown_wood.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "white wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/white_wood.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "bright wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/bright_wood.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "gray wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/gray_wood.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    if subject == "light blue wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/light-blue-gray_wood.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        panel = tk.Label(window, background="white", image=im2)
        panel.pack()
    window.mainloop()


# crops the image and remove the background
def cut(data, category):
    im = cv2.imread(data)
    r = cv2.selectROI(im) # the user marks in the image the area of the object
    imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    a = int(r[0]) # the x rate of the top left point
    b = int(r[1]) # the y rate of the top left point
    c = int(r[0] + r[2]) - int(r[0]) # the width of the area
    d = int(r[1] + r[3]) - int(r[1]) # the height of the area
    cv2.destroyAllWindows()

    img = cv2.imread(data)
    mask = np.zeros(img.shape[:2], np.uint8) # returns a new array of given shape and type where the element's value as 0

    bgModel = np.zeros((1, 65), np.float64) # the temporary array used to model the background
    fgModel = np.zeros((1, 65), np.float64) # the temporary array for the foreground

    rect = (a,b,c,d) # the bounding box rectangle that contains the region that the user wants to segment

    cv2.grabCut(img, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT) # cut the image and do mask

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8') # the foreground mask, pixel is 0 if it is background else 1
    img = img * mask2[:, :, np.newaxis] # combines between the image and the mask

    s = backgrounds_screen1(img, category)
    if s == "back" or s == "exit":
        arr = s
    else:
        arr = [a, b, c, d, s[0], s[1]]
    return arr


# shows screen with buttons of the backgrounds by categories and the user need choose a background
def backgrounds_screen3(category):
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

    smallfont = pygame.font.Font('freesansbold.ttf', 30)

    if category == "thing":

        smallfont = pygame.font.Font('freesansbold.ttf', 30)

        text1 = smallfont.render('Forest', True, (255, 255, 255))
        text2 = smallfont.render('Lawn', True, (255, 255, 255))
        text3 = smallfont.render('Sky', True, (255, 255, 255))
        text4 = smallfont.render('Wall', True, (0, 0, 0))
        text5 = smallfont.render('White-Wood', True, (0, 0, 0))
        text6 = smallfont.render('Brown-Wood', True, (255, 255, 255))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 130 <= mouse[0] <= 130 + 110 and 90 <= mouse[1] <= 90 + 50:
                        return "forest"
                    if 490 <= mouse[0] <= 490 + 100 and 90 <= mouse[1] <= 90 + 50:
                        return "lawn"
                    if 150 <= mouse[0] <= 150 + 80 and 210 <= mouse[1] <= 210 + 50:
                        return "sky"
                    if 500 <= mouse[0] <= 500 + 80 and 210 <= mouse[1] <= 210 + 50:
                        return "wall"
                    if 85 <= mouse[0] <= 85 + 200 and 330 <= mouse[1] <= 330 + 50:
                        return "white wood"
                    if 435 <= mouse[0] <= 435 + 210 and 330 <= mouse[1] <= 330 + 50:
                        return "brown wood"
            pygame.draw.rect(screen, (50, 156, 10), [130, 90, 110, 50])
            pygame.draw.rect(screen, (73, 173, 14), [490, 90, 100, 50])
            pygame.draw.rect(screen, (104, 38, 102), [150, 210, 80, 50])
            pygame.draw.rect(screen, (197, 197, 197), [500, 210, 80, 50])
            pygame.draw.rect(screen, (255, 255, 255), [85, 330, 200, 50])
            pygame.draw.rect(screen, (89, 45, 0), [435, 330, 210, 50])
            screen.blit(text1, (140, 100))
            screen.blit(text2, (500, 100))
            screen.blit(text3, (160, 220))
            screen.blit(text4, (510, 220))
            screen.blit(text5, (95, 340))
            screen.blit(text6, (445, 340))
            pygame.display.flip()

    if category == "food":
        text1 = smallfont.render('brown wood', True, (255, 255, 255))
        text2 = smallfont.render('white wood', True, (0, 0, 0))
        text3 = smallfont.render('bright wood', True, (255, 255, 255))
        text4 = smallfont.render('gray wood', True, (255, 255, 255))
        text5 = smallfont.render('light blue wood', True, (255, 255, 255))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 90 <= mouse[0] <= 90 + 195 and 90 <= mouse[1] <= 90 + 50:
                        return "brown wood"
                    if 440 <= mouse[0] <= 440 + 185 and 90 <= mouse[1] <= 90 + 50:
                        return "white wood"
                    if 90 <= mouse[0] <= 90 + 195 and 210 <= mouse[1] <= 210 + 50:
                        return "bright wood"
                    if 440 <= mouse[0] <= 440 + 185 and 210 <= mouse[1] <= 210 + 50:
                        return "gray wood"
                    if 240 <= mouse[0] <= 240 + 250 and 330 <= mouse[1] <= 330 + 50:
                        return "light blue wood"
            pygame.draw.rect(screen, (89, 45, 0), [90, 90, 195, 50])
            pygame.draw.rect(screen, (255, 255, 255), [440, 90, 185, 50])
            pygame.draw.rect(screen, (189, 136, 104), [90, 210, 195, 50])
            pygame.draw.rect(screen, (160, 177, 188), [440, 210, 185, 50])
            pygame.draw.rect(screen, (121, 181, 189), [240, 330, 250, 50])
            screen.blit(text1, (100, 100))
            screen.blit(text2, (450, 100))
            screen.blit(text3, (100, 220))
            screen.blit(text4, (460, 220))
            screen.blit(text5, (255, 340))
            pygame.display.flip()

    if category == "animal":
        text1 = smallfont.render('Desert', True, (255, 255, 255))
        text2 = smallfont.render('Forest', True, (255, 255, 255))
        text3 = smallfont.render('Lawn', True, (255, 255, 255))
        text4 = smallfont.render('Snow', True, (0, 0, 0))
        text5 = smallfont.render('Sky', True, (255, 255, 255))
        text6 = smallfont.render('Road', True, (255, 255, 255))
        text7 = smallfont.render('Wall', True, (0, 0, 0))
        text8 = smallfont.render('Pathway', True, (0, 0, 0))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 60 <= mouse[0] <= 60 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return "desert"
                    if 220 <= mouse[0] <= 220 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return "forest"
                    if 370 <= mouse[0] <= 370 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return "lawn"
                    if 525 <= mouse[0] <= 525 + 120 and 140 <= mouse[1] <= 140 + 50:
                        return "snow"
                    if 60 <= mouse[0] <= 60 + 120 and 290 <= mouse[1] <= 290 + 50:
                        return "sky"
                    if 220 <= mouse[0] <= 220 + 120 and 290 <= mouse[1] <= 290 + 50:
                        return "road"
                    if 370 <= mouse[0] <= 370 + 120 and 290 <= mouse[1] <= 290 + 50:
                        return "wall"
                    if 505 <= mouse[0] <= 505 + 140 and 290 <= mouse[1] <= 290 + 50:
                        return "pathway"
            pygame.draw.rect(screen, (140, 70, 0), [60, 140, 120, 50])
            pygame.draw.rect(screen, (50, 156, 10), [220, 140, 120, 50])
            pygame.draw.rect(screen, (73, 173, 14), [370, 140, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [525, 140, 120, 50])
            pygame.draw.rect(screen, (104, 38, 102), [60, 290, 120, 50])
            pygame.draw.rect(screen, (66, 77, 79), [220, 290, 120, 50])
            pygame.draw.rect(screen, (197, 197, 197), [370, 290, 120, 50])
            pygame.draw.rect(screen, (255, 231, 206), [505, 290, 140, 50])
            screen.blit(text1, (70, 150))
            screen.blit(text2, (235, 150))
            screen.blit(text3, (390, 150))
            screen.blit(text4, (545, 150))
            screen.blit(text5, (90, 300))
            screen.blit(text6, (245, 300))
            screen.blit(text7, (400, 300))
            screen.blit(text8, (512, 300))
            pygame.display.flip()

    if category == "vehicle":
        text1 = smallfont.render('Garage 1', True, (255, 255, 255))
        text2 = smallfont.render('Garage 2', True, (255, 255, 255))
        text3 = smallfont.render('Outside Parking 1', True, (255, 255, 255))
        text4 = smallfont.render('Outside Parking 2', True, (255, 255, 255))
        text5 = smallfont.render('Underground Parking', True, (255, 255, 255))
        text6 = smallfont.render('Pathway', True, (0, 0, 0))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 90 <= mouse[0] <= 90 + 150 and 90 <= mouse[1] <= 90 + 50:
                        return "garage1"
                    if 460 <= mouse[0] <= 460 + 150 and 90 <= mouse[1] <= 90 + 50:
                        return "garage2"
                    if 40 <= mouse[0] <= 40 + 290 and 210 <= mouse[1] <= 210 + 50:
                        return "parking1"
                    if 370 <= mouse[0] <= 370 + 290 and 210 <= mouse[1] <= 210 + 50:
                        return "parking2"
                    if 70 <= mouse[0] <= 70 + 340 and 330 <= mouse[1] <= 330 + 50:
                        return "parking3"
                    if 490 <= mouse[0] <= 490 + 140 and 330 <= mouse[1] <= 330 + 50:
                        return "pathway"
            pygame.draw.rect(screen, (139, 139, 139), [90, 90, 150, 50])
            pygame.draw.rect(screen, (90, 90, 90), [460, 90, 150, 50])
            pygame.draw.rect(screen, (191, 191, 191), [40, 210, 290, 50])
            pygame.draw.rect(screen, (112, 112, 112), [370, 210, 290, 50])
            pygame.draw.rect(screen, (141, 141, 141), [70, 330, 340, 50])
            pygame.draw.rect(screen, (255, 231, 206), [490, 330, 140, 50])
            screen.blit(text1, (100, 100))
            screen.blit(text2, (468, 100))
            screen.blit(text3, (50, 220))
            screen.blit(text4, (380, 220))
            screen.blit(text5, (80, 340))
            screen.blit(text6, (500, 340))
            pygame.display.flip()

    if category == "person":
        text1 = smallfont.render('Beach', True, (255, 255, 255))
        text2 = smallfont.render('Lawn', True, (255, 255, 255))
        text3 = smallfont.render('Snow', True, (0, 0, 0))
        text4 = smallfont.render('Sky', True, (255, 255, 255))
        text5 = smallfont.render('Road', True, (255, 255, 255))
        text6 = smallfont.render('Park', True, (255, 255, 255))
        text7 = smallfont.render('Pathway', True, (0, 0, 0))

        pygame.display.flip()
        # the buttons on the screen
        finish = False
        while not finish:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 90 <= mouse[0] <= 90 + 120 and 90 <= mouse[1] <= 90 + 50:
                        return "beach"
                    if 290 <= mouse[0] <= 290 + 120 and 90 <= mouse[1] <= 90 + 50:
                        return "lawn"
                    if 490 <= mouse[0] <= 490 + 120 and 90 <= mouse[1] <= 90 + 50:
                        return "snow"
                    if 90 <= mouse[0] <= 90 + 120 and 210 <= mouse[1] <= 210 + 50:
                        return "sky"
                    if 290 <= mouse[0] <= 290 + 120 and 210 <= mouse[1] <= 210 + 50:
                        return "road"
                    if 490 <= mouse[0] <= 490 + 120 and 210 <= mouse[1] <= 210 + 50:
                        return "park"
                    if 280 <= mouse[0] <= 280 + 140 and 330 <= mouse[1] <= 330 + 50:
                        return "pathway"
            pygame.draw.rect(screen, (66, 216, 253), [90, 90, 120, 50])
            pygame.draw.rect(screen, (73, 173, 14), [290, 90, 120, 50])
            pygame.draw.rect(screen, (255, 255, 255), [490, 90, 120, 50])
            pygame.draw.rect(screen, (104, 38, 102), [90, 210, 120, 50])
            pygame.draw.rect(screen, (66, 77, 79), [290, 210, 120, 50])
            pygame.draw.rect(screen, (103, 236, 23), [490, 210, 120, 50])
            pygame.draw.rect(screen, (255, 231, 206), [280, 330, 140, 50])
            screen.blit(text1, (105, 100))
            screen.blit(text2, (310, 100))
            screen.blit(text3, (510, 100))
            screen.blit(text4, (117, 220))
            screen.blit(text5, (312, 220))
            screen.blit(text6, (517, 220))
            screen.blit(text7, (290, 340))
            pygame.display.flip()


# cut("C:/Users/IMOE001/Downloads/image17.jpg", "thing")