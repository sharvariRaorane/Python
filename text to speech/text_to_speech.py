
from gtts import gTTS
import os
from tkinter import *

def textToSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text,lang=language,slow=FALSE)
    output.save('output.mp3')
    os.system("start output.mp3")

root = Tk()

canvas = Canvas(root,width=400,height=300)
canvas.pack()

entry = Entry(root)
canvas.create_window(200,180,window=entry)

button = Button(text='Start',command=textToSpeech)
canvas.create_window(200,230,window=button)

root.mainloop()