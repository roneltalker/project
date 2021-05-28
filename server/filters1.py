from PIL import Image, ImageFilter, ImageEnhance, ImageChops
import numpy as np


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


# selects the filter selected by the user
def filt(image, subject):
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
        img_flipped = Image.fromarray(img_flipped_data)
        return img_flipped
    if subject == "black-white":
        im1 = im.convert(mode='L')
        return im1
    if subject == "black-white contours":
        im1 = (im.convert(mode='L')).filter(ImageFilter.CONTOUR)
        return im1
    if subject == "increasing contours":
        im1 = im.filter(ImageFilter.EDGE_ENHANCE)
        return im1
    if subject == "light":
        im1 = im.filter(ImageFilter.MaxFilter(size=3))
        return im1
    if subject == "water color":
        im1 = im.filter(ImageFilter.ModeFilter(size=6))
        return im1
    if subject == "contrast":
        im1 = enh.enhance(1.5)
        return im1
    if subject == "darkness":
        im1 = enh.enhance(0.6)
        return im1
    if subject == "contours":
        im1 = im.filter(ImageFilter.CONTOUR)
        return im1
    if subject == "red":
        im1 = imgR
        return im1
    if subject == "night":
        im1 = ImageChops.invert(im)
        return im1
    if subject == "dark":
        im1 = im.filter(ImageFilter.MinFilter(size=3))
        return im1
    if subject == "black-white binary":
        bin_im = get_binary_image(im, 100)
        im1 = bin_im
        return im1
    if subject == "high increasing contours":
        im1 = im.filter(ImageFilter.UnsharpMask( radius=3, percent=250, threshold=4))
        return im1
    if subject == "high darkness":
        im1 = enh.enhance(0.3)
        return im1
    if subject == "blurred":
        im1 = im.filter(ImageFilter.BLUR)
        return im1
    if subject == "green":
        im1 = imgG
        return im1
    if subject == "higher contrast":
        im1 = enh.enhance(1.8)
        return im1