import socket
from yolo import detection
import cv2
from background1 import backgrounds
import numpy as np
from filters1 import filt
from frame1 import frame
import pygame
from PIL import Image


# accepts the user's selections and acts accordingly
def func1(path):
    button = client_socket.recv(1024) # the tool selected by the user
    button = button.decode()
    # if the user exits the software the communication ends
    if button == 'exit':
        client_socket.close()
        server_socket.close()
    else:
        print(button)
        but = button.encode()
        client_socket.send(but)
        l = path.split("/")
        if l[-1] != "new.jpg":
            # saves the edited image in the file of the original image as "new"
            l.remove(l[-1])
            l.append("new.jpg")
            new = '/'.join(l)
        else:
            new = path

        if button == "cut":
            a = client_socket.recv(1024) # the y rate of the top left point of the cropped image
            a = a.decode()
            # if the user exits the software the communication ends
            if a == 'exit':
                client_socket.close()
                server_socket.close()
            else:
                aa = a.encode()
                client_socket.send(aa)
                # if the user clicks on "back" button, the screen is the tools screen
                if a == "back":
                    func1(path)
                else:
                    b = client_socket.recv(1024) # the height of the cropped image
                    b = b.decode()
                    bb = b.encode()
                    client_socket.send(bb)
                    c = client_socket.recv(1024) # the x rate of the top left point of the cropped image
                    c = c.decode()
                    cc = c.encode()
                    client_socket.send(cc)
                    d = client_socket.recv(1024) # the width of the cropped image
                    d = d.decode()
                    dd = d.encode()
                    client_socket.send(dd)
                    s = client_socket.recv(1024) # the choose of the user- "save and continue" or "save and exit"
                    s = s.decode()
                    ss = s.encode()
                    client_socket.send(ss)
                    img = cv2.imread(path)
                    img = img[int(a):int(b), int(c):int(d)] # crops the image
                    opencv_image = img[:, :,::-1]  # Since OpenCV is BGR and pygame is RGB, it is necessary to convert it.
                    shape = opencv_image.shape[1::-1]  # OpenCV(height,width,Number of colors), Pygame(width, height)So this is also converted.
                    img = pygame.image.frombuffer(opencv_image.tobytes(), shape, 'RGB')
                    pygame.image.save(img, new)
                    if s == "save and continue":
                        a = new.encode()
                        client_socket.send(a)
                        aa = client_socket.recv(1024)
                        aa = aa.decode()
                        func1(new) # back to the tools screen

        if button == "background":
            a = client_socket.recv(1024) # the x rate of the top left point of the cropped image
            a = a.decode()
            # if the user exits the software the communication ends
            if a == 'exit':
                client_socket.close()
                server_socket.close()
            else:
                aa = a.encode()
                client_socket.send(aa)
                # if the user clicks on "back" button, the screen is the tools screen
                if a == "back":
                    func1(path)
                else:
                    b = client_socket.recv(1024) # the y rate of the top left point of the cropped image
                    b = b.decode()
                    bb = b.encode()
                    client_socket.send(bb)
                    c = client_socket.recv(1024) # the width of the cropped image
                    c = c.decode()
                    cc = c.encode()
                    client_socket.send(cc)
                    d = client_socket.recv(1024) # the height of the cropped image
                    d = d.decode()
                    dd = d.encode()
                    client_socket.send(dd)
                    s1 = client_socket.recv(1024) # the background image that the user selected
                    s1 = s1.decode()
                    ss1 = s1.encode()
                    client_socket.send(ss1)
                    s2 = client_socket.recv(1024) # the choose of the user- "save and continue" or "save and exit"
                    s2 = s2.decode()
                    ss2 = s2.encode()
                    client_socket.send(ss2)
                    img = cv2.imread(path)
                    mask = np.zeros(img.shape[:2], np.uint8) # returns a new array of given shape and type where the element's value as 0
                    bgModel = np.zeros((1, 65), np.float64) # the temporary array used to model the background
                    fgModel = np.zeros((1, 65), np.float64) # the temporary array for the foreground
                    rect = (int(a), int(b), int(c), int(d)) # the bounding box rectangle that contains the region that the user wants to segment
                    cv2.grabCut(img, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT) # crops the image and do mask
                    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8') # the foreground mask, pixel is 0 if it is background else 1
                    img = img * mask2[:, :, np.newaxis] # combines between the image and the mask
                    img = backgrounds(img, s1) # the new image after the changing the background
                    img.save(new)
                    if s2 == "save and continue":
                        a = new.encode()
                        client_socket.send(a)
                        aa = client_socket.recv(1024)
                        aa = aa.decode()
                        func1(new) # back to the tools screen

        if button == "filter":
            f1 = client_socket.recv(1024) # the filter that the user selected
            f1 = f1.decode()
            # if the user exits the software the communication ends
            if f1 == 'exit':
                client_socket.close()
                server_socket.close()
            else:
                ff1 = f1.encode()
                client_socket.send(ff1)
                # if the user clicks on "back" button, the screen is the tools screen
                if f1 == "back":
                    func1(path)
                else:
                    f2 = client_socket.recv(1024) # the choose of the user- "save and continue" or "save and exit"
                    f2 = f2.decode()
                    ff2 = f2.encode()
                    client_socket.send(ff2)
                    img = filt(path, f1) # the new image after the putting the filter
                    img.save(new)
                    if f2 == "save and continue":
                        a = new.encode()
                        client_socket.send(a)
                        aa = client_socket.recv(1024)
                        aa = aa.decode()
                        func1(new) # back to the tools screen

        if button == "frame":
            r1 = client_socket.recv(1024) # the number of the frame that the user selected
            r1 = r1.decode()
            # if the user exits the software the communication ends
            if r1 == 'exit':
                client_socket.close()
                server_socket.close()
            else:
                rr1 = r1.encode()
                client_socket.send(rr1)
                # if the user clicks on "back" button, the screen is the tools screen
                if r1 == "back":
                    func1(path)
                else:
                    r2 = client_socket.recv(1024) # the choose of the user- "save and continue" or "save and exit"
                    r2 = r2.decode()
                    rr2 = r2.encode()
                    client_socket.send(rr2)
                    img = frame(path, int(r1)) # the new image after the adding the frame
                    img.save(new)
                    if r2 == "save and continue":
                        a = new.encode()
                        client_socket.send(a)
                        aa = client_socket.recv(1024)
                        aa = aa.decode()
                        func1(new) # back to the tools screen


server_socket = socket.socket()
ip = "127.0.0.1" # the ip of the server
port = 4000 # the port of the server
server_socket.bind((ip, port))
server_socket.listen(1)
print("Server online")
client_socket, client_address = server_socket.accept()
print("client address: ", client_address) # the address of the client
path = client_socket.recv(1024) # the path of the image that the user choose
path = path.decode()
# if the user exits the software the communication ends
if path == 'exit':
    client_socket.close()
    server_socket.close()
else:
    print("The path of the image which send by the client is: ", path)
    baseheight = 350 # sets image height
    img = Image.open(path)
    hpercent = (baseheight / float(img.size[1])) # image aspect ratio
    wsize = int((float(img.size[0]) * float(hpercent))) # calculates the width of the image
    img = img.resize((wsize, baseheight), Image.ANTIALIAS) # changes the dimensions of the image
    img.save(path) # the image is saved in the new size
    mes = path
    mes1 = mes.encode()
    client_socket.send(mes1)
    category = detection(mes) # the category of the object in the image
    print("The type of the object which in the image is: ", category)
    category = category.encode()
    client_socket.send(category)
    button = client_socket.recv(1024) # the tool selected by the user
    button = button.decode()
    print(button)
    but = button.encode()
    client_socket.send(but)
    func1(path)
    # the communication ends
    client_socket.close()
    server_socket.close()
