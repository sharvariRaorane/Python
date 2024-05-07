from tkinter import *
import pyqrcode
from PIL import Image, ImageTk
import png 

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    filename = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(filename,scale=8)
    image = ImageTk.PhotoImage(Image.open(filename))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,450,window=image_label)

root = Tk()

canvas = Canvas(root, width=400,height=600)
canvas.pack()

label = Label(root,text = "QR Code", fg='blue',font=("Arial",30))

canvas.create_window(200,50,window=label)

name_label = Label(root,text = "Link Name")
link_label = Label(root,text = "Link")
canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200,120,window=name_entry)
canvas.create_window(200,180,window=link_entry)

button = Button(text="Generate QRCode",command=generate)
canvas.create_window(200,220,window=button)

root.mainloop()