import socket
from screen import first_screen
from yolo import screen1, screen2
from buttons1 import options_instructions1
from buttons import options_screen
from PIL import Image
import subprocess


# accepts the user's selections and sends to server
def func(data2, button, mes):
    button1 = button.encode()
    my_socket.send(button1)
    data4 = my_socket.recv(1024)
    data4 = data4.decode()
    arr = options_instructions1(mes, button, data2)
    # if the user clicks on "back" button, the screen is the tools screen
    if arr == "back":
        arr = arr.encode()
        my_socket.send(arr)
        data5 = my_socket.recv(1024)
        data5 = data5.decode()
        button = options_screen()
        func(data2, button, mes)
    elif button == "cut":
        # if the user exits the software the communication ends
        if arr == "exit":
            arr = arr.encode()
            my_socket.send(arr)
            my_socket.close()
        else:
            a = str(arr[0]) # the y rate of the top left point of the cropped image
            a = a.encode()
            my_socket.send(a)
            aa = my_socket.recv(1024)
            aa = aa.decode()
            b = str(arr[1]) # the height of the cropped image
            b = b.encode()
            my_socket.send(b)
            bb = my_socket.recv(1024)
            bb = bb.decode()
            c = str(arr[2]) # the x rate of the top left point of the cropped image
            c = c.encode()
            my_socket.send(c)
            cc = my_socket.recv(1024)
            cc = cc.decode()
            d = str(arr[3]) # the width of the cropped image
            d = d.encode()
            my_socket.send(d)
            dd = my_socket.recv(1024)
            dd = dd.decode()
            s = arr[4] # the choose of the user- "save and continue" or "save and exit"
            s = s.encode()
            my_socket.send(s)
            ss = my_socket.recv(1024)
            ss = ss.decode()
            if arr[4] == "save and continue":
                img = my_socket.recv(1024) # the path of the edited image
                img = img.decode()
                img1 = img.encode()
                my_socket.send(img1)
                # back to the tools screen
                button = options_screen()
                func(data2, button, img)
    elif button == "background":
        # if the user exits the software the communication ends
        if arr == "exit":
            arr = arr.encode()
            my_socket.send(arr)
            my_socket.close()
        else:
            a = str(arr[0]) # the x rate of the top left point of the cropped image
            a = a.encode()
            my_socket.send(a)
            aa = my_socket.recv(1024)
            aa = aa.decode()
            b = str(arr[1]) # the y rate of the top left point of the cropped image
            b = b.encode()
            my_socket.send(b)
            bb = my_socket.recv(1024)
            bb = bb.decode()
            c = str(arr[2]) # the width of the cropped image
            c = c.encode()
            my_socket.send(c)
            cc = my_socket.recv(1024)
            cc = cc.decode()
            d = str(arr[3]) # the height of the cropped image
            d = d.encode()
            my_socket.send(d)
            dd = my_socket.recv(1024)
            dd = dd.decode()
            s1 = arr[4] # the background image that the user selected
            s1 = s1.encode()
            my_socket.send(s1)
            ss1 = my_socket.recv(1024)
            ss1 = ss1.decode()
            s2 = arr[5] # the choose of the user- "save and continue" or "save and exit"
            s2 = s2.encode()
            my_socket.send(s2)
            ss2 = my_socket.recv(1024)
            ss2 = ss2.decode()
            if arr[5] == "save and continue":
                img = my_socket.recv(1024) # the path of the edited image
                img = img.decode()
                img1 = img.encode()
                my_socket.send(img1)
                # back to the tools screen
                button = options_screen()
                func(data2, button, img)
    elif button == "filter":
        # if the user exits the software the communication ends
        if arr == "exit":
            arr = arr.encode()
            my_socket.send(arr)
            my_socket.close()
        else:
            a = (arr[0]).encode() # the filter that the user selected
            my_socket.send(a)
            aa = my_socket.recv(1024)
            aa = aa.decode()
            b = (arr[1]).encode() # the choose of the user- "save and continue" or "save and exit"
            my_socket.send(b)
            bb = my_socket.recv(1024)
            bb = bb.decode()
            if arr[1] == "save and continue":
                img = my_socket.recv(1024) # the path of the edited image
                img = img.decode()
                img1 = img.encode()
                my_socket.send(img1)
                # back to the tools screen
                button = options_screen()
                func(data2, button, img)
    elif button == "frame":
        # if the user exits the software the communication ends
        if arr == "exit":
            arr = arr.encode()
            my_socket.send(arr)
            my_socket.close()
        else:
            r1 = str(arr[0]) # the number of the frame that the user selected
            r1 = r1.encode()
            my_socket.send(r1)
            rr1 = my_socket.recv(1024)
            rr1 = rr1.decode()
            r2 = arr[1] # the choose of the user- "save and continue" or "save and exit"
            r2 = r2.encode()
            my_socket.send(r2)
            rr2 = my_socket.recv(1024)
            rr2 = rr2.decode()
            if arr[1] == "save and continue":
                img = my_socket.recv(1024) # the path of the edited image
                img = img.decode()
                img1 = img.encode()
                my_socket.send(img1)
                # back to the tools screen
                button = options_screen()
                func(data2, button, img)


# installs the libraries of the project
libraries = ["Pillow", "opencv-python", "numpy", "pygame", "PyQt5", "imageai", "tensorflow"]
for library in libraries:
    subprocess.check_output("pip install " + library, shell=True)

# connects to the server
ip = '127.0.0.1' # the ip of the server
port = 4000 # the port of the server
my_socket = socket.socket()
my_socket.connect((ip, port))
print("ip: ", ip, ", port: ", port)
mes = first_screen() # shows the user the opening screen
if mes == 'exit':
    mes = mes.encode()
    my_socket.send(mes)
    my_socket.close()
else:
    baseheight = 350 # sets image height
    img = Image.open(mes)
    hpercent = (baseheight / float(img.size[1])) # image aspect ratio
    wsize = int((float(img.size[0]) * float(hpercent))) # calculates the width of the image
    img = img.resize((wsize, baseheight), Image.ANTIALIAS) # changes the dimensions of the image
    img.save(mes)
    mes1 = mes.encode()
    my_socket.send(mes1)
    data1 = my_socket.recv(1024)
    data1 = data1.decode()
    screen1()
    data2 = my_socket.recv(1024)
    data2 = data2.decode()
    button = screen2(data2) # the tool selected by the user
    button1 = button.encode()
    my_socket.send(button1)
    data3 = my_socket.recv(1024)
    data3 = data3.decode()
    func(data2, button, mes)
    my_socket.close()