from PIL import Image, ImageTk
import cv2


# removes the background in the image and switches to another background
def change_backrounds(img, bg):
    img2 = img
    src = cv2.imread(bg, cv2.IMREAD_UNCHANGED) # loads the background image
    width = img2.shape[1] # the width of the image
    height = img2.shape[0] # the height of the image
    dsize = (width, height) # the size of the image
    output = cv2.resize(src, dsize) # the size of the new image is the same as the size of the original image
    cv2.imwrite(bg, output) # saves the background image in the new size
    img1 = cv2.imread(bg) # the background image in the new size
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) # converts the image from RGB to grayscale
    # cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) =  if the pixel value is smaller from 10 it is black, else white
    # ret is the threshold (10)
    # mask is the threshold image
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask) # creates inverted mask for background

    # black-out the area of the object in the image in the background image
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # takes only region of the object in the image
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # puts the object in the image in the background image and modify the image
    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst
    return cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) # preserves the original image color


# selects the background selected by the user
def backgrounds(img, subject):
    if subject == "beach":
        im1 = Image.fromarray(change_backrounds(img, 'images/beach.png'))
        return im1
    if subject == "lawn":
        im1 = Image.fromarray(change_backrounds(img, 'images/lawn.jpg'))
        return im1
    if subject == "snow":
        im1 = Image.fromarray(change_backrounds(img, 'images/snow.jpg'))
        return im1
    if subject == "sky":
        im1 = Image.fromarray(change_backrounds(img, 'images/sky.jpg'))
        return im1
    if subject == "road":
        im1 = Image.fromarray(change_backrounds(img, 'images/road.jpg'))
        return im1
    if subject == "park":
        im1 = Image.fromarray(change_backrounds(img, 'images/park.jpg'))
        return im1
    if subject == "pathway":
        im1 = Image.fromarray(change_backrounds(img, 'images/pathway.jpg'))
        return im1
    if subject == "garage1":
        im1 = Image.fromarray(change_backrounds(img, 'images/garage_1.jpg'))
        return im1
    if subject == "garage2":
        im1 = Image.fromarray(change_backrounds(img, 'images/garage_2.jpg'))
        return im1
    if subject == "parking1":
        im1 = Image.fromarray(change_backrounds(img, 'images/parking_1.jpg'))
        return im1
    if subject == "parking2":
        im1 = Image.fromarray(change_backrounds(img, 'images/parking_2.jpg'))
        return im1
    if subject == "parking3":
        im1 = Image.fromarray(change_backrounds(img, 'images/parking_3.jpg'))
        im2 = ImageTk.PhotoImage(im1)
        return im2
    if subject == "desert":
        im1 = Image.fromarray(change_backrounds(img, 'images/desert.jpg'))
        return im1
    if subject == "forest":
        im1 = Image.fromarray(change_backrounds(img, 'images/forest.jpg'))
        return im1
    if subject == "wall":
        im1 = Image.fromarray(change_backrounds(img, 'images/wall.jpg'))
        return im1
    if subject == "brown wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/brown_wood.jpg'))
        return im1
    if subject == "white wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/white_wood.jpg'))
        return im1
    if subject == "bright wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/bright_wood.jpg'))
        return im1
    if subject == "gray wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/gray_wood.jpg'))
        return im1
    if subject == "light blue wood":
        im1 = Image.fromarray(change_backrounds(img, 'images/light-blue-gray_wood.jpg'))
        return im1