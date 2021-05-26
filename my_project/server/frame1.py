from PIL import Image, ImageOps


# creates frames
def frames(im, color, a, b, c, d):
    img = im
    border = (a, b, c, d)

    new_img = ImageOps.expand(img, border=border, fill=color)

    return new_img


# selects the frame selected by the user
def frame(img, number):
    img = Image.open(img)
    img.thumbnail((250, 250))
    if number == 1:
        img1 = frames(img, "black", 10, 10, 10, 10)
        return img1
    if number == 2:
        img1 = frames(img, "black", 10, 20, 10, 20)
        return img1
    if number == 3:
        img1 = frames(img, "black", 20, 10, 20, 10)
        return img1
    if number == 4:
        img1 = frames(img, "gray", 10, 10, 10, 10)
        return img1
    if number == 5:
        img1 = frames(img, "gray", 10, 20, 10, 20)
        return img1
    if number == 6:
        img1 = frames(img, "gray", 20, 10, 20, 10)
        return img1
    if number == 7:
        img1 = frames(img, "blue", 10, 10, 10, 10)
        return img1
    if number == 8:
        img1 = frames(img, "blue", 10, 20, 10, 20)
        return img1
    if number == 9:
        img1 = frames(img, "blue", 20, 10, 20, 10)
        return img1
    if number == 10:
        img1 = frames(img, "red", 10, 10, 10, 10)
        return img1
    if number == 11:
        img1 = frames(img, "red", 10, 20, 10, 20)
        return img1
    if number == 12:
        img1 = frames(img, "red", 20, 10, 20, 10)
        return img1
    if number == 13:
        img1 = frames(img, "green", 10, 10, 10, 10)
        return img1
    if number == 14:
        img1 = frames(img, "green", 10, 20, 10, 20)
        return img1
    if number == 15:
        img1 = frames(img, "green", 20, 10, 20, 10)
        return img1
    if number == 16:
        img1 = frames(img, "yellow", 10, 10, 10, 10)
        return img1
    if number == 17:
        img1 = frames(img, "yellow", 10, 20, 10, 20)
        return img1
    if number == 18:
        img1 = frames(img, "yellow", 20, 10, 20, 10)
        return img1
    if number == 19:
        img1 = frames(img, "purple", 10, 10, 10, 10)
        return img1
    if number == 20:
        img1 = frames(img, "purple", 10, 20, 10, 20)
        return img1
    if number == 21:
        img1 = frames(img, "purple", 20, 10, 20, 10)
        return img1
    if number == 22:
        img1 = frames(img, "pink", 10, 10, 10, 10)
        return img1
    if number == 23:
        img1 = frames(img, "pink", 10, 20, 10, 20)
        return img1
    if number == 24:
        img1 = frames(img, "pink", 20, 10, 20, 10)
        return img1
    if number == 25:
        img1 = frames(img, "orange", 10, 10, 10, 10)
        return img1
    if number == 26:
        img1 = frames(img, "orange", 10, 20, 10, 20)
        return img1
    if number == 27:
        img1 = frames(img, "orange", 20, 10, 20, 10)
        return img1
    if number == 28:
        img1 = frames(img, "brown", 10, 10, 10, 10)
        return img1
    if number == 29:
        img1 = frames(img, "brown", 10, 20, 10, 20)
        return img1
    if number == 30:
        img1 = frames(img, "brown", 20, 10, 20, 10)
        return img1