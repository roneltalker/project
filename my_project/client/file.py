from PyQt5.QtWidgets import *


# checks if the user has selected an image
def i():
    list1 = [] # list of the images
    image1, l1 = load_file()
    list1.append(image1)
    # if the user didn't select an image than he has to select again
    while l1 != 'jpg' and l1 != 'jpeg' and l1 != 'png':
        print("You didn't select an image. You need select an image. Try again.")
        image2, l1 = load_file()
        list1.append(image2)
    return list1


# opens the files on the computer and the user has to select an image
def load_file():
    fname = QFileDialog.getOpenFileName(None, "Select File")[0] # opens the files and returns a file that the user selected
    img = open(fname, 'r', encoding='utf-8')
    list = (str(img)).split() # the list with the details of the image
    print(list)
    print(list[1:-2]) # the location of the path pf the image in the list
    lis = (' '.join(list[1:-2])).split("=") # the list of the path of the image
    print(lis)
    li = lis[1].split("'") # the list with the path of the image
    image = li[1] # the path of the image
    print(image)
    l = li[1].split(".") # the list that separates between the path and the type of the image
    print(l)
    return image, l[1] # the path of the image and the type of the image
