import cv2
import pygame


# crops the image
def cutting(data):
    im = cv2.imread(data)
    r = cv2.selectROI(im) # the user marks in the image the area he wants to cut
    crop_img = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    a = int(r[1]) # the y rate of the top left point
    b = int(r[1] + r[3]) # the height of the area
    c = int(r[0]) # the x rate of the top left point
    d = int(r[0] + r[2]) # the width of the area
    cv2.destroyAllWindows()

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
    color_light1 = (0, 0, 0)
    textt3 = smallfont.render('Choose & Exit', True, (255, 255, 255))
    textt2 = smallfont.render('Choose & Continue', True, (255, 255, 255))
    textt1 = smallfont.render('back', True, (255, 255, 255))

    crop_image1 = convert_opencv_img_to_pygame(crop_img)
    screen.blit(crop_image1, (50, 50))
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
                if 440 <= mouse[0] <= 440 + 230 and 420 <= mouse[1] <= 420 + 50:
                    return [a, b, c, d, "save and exit"]
                if 130 <= mouse[0] <= 130 + 300 and 420 <= mouse[1] <= 420 + 50:
                    return [a, b, c, d, "save and continue"]
                if 30 <= mouse[0] <= 30 + 90 and 420 <= mouse[1] <= 420 + 50:
                    return "back"
        pygame.draw.rect(screen, color_light1, [440, 420, 230, 50])
        pygame.draw.rect(screen, color_light1, [130, 420, 300, 50])
        pygame.draw.rect(screen, color_light1, [30, 420, 90, 50])
        screen.blit(textt3, (450, 430))
        screen.blit(textt2, (140, 430))
        screen.blit(textt1, (40, 430))
        pygame.display.flip()

    return a, b, c, d


# convert opencv image to pygame image
def convert_opencv_img_to_pygame(opencv_image):
    opencv_image = opencv_image[:,:,::-1]  # Since OpenCV is BGR and pygame is RGB, it is necessary to convert it.
    shape = opencv_image.shape[1::-1]  # OpenCV(height,width,Number of colors), Pygame(width, height)So this is also converted.
    pygame_image = pygame.image.frombuffer(opencv_image.tobytes(), shape, 'RGB')

    return pygame_image


# cutting("C:/Users/IMOE001/Downloads/image6.jpg")
