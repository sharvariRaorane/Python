from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

root = Tk()
root.title("YouTube Video Downloader")

canvas = Canvas(root,width=500,height=400)
canvas.pack()

# appLabel
appLabel = Label(root,text="Video Downloader",font=("Times New Roman",21))
canvas.create_window(250,20,window=appLabel)

# videoURL
urlLabel = Label(root,text="Enter URL:")
canvas.create_window(250,60,window=urlLabel)
urlEntry = Entry(root)
canvas.create_window(250,80,window=urlEntry)

# get_location fuction
def get_location():
    location = filedialog.askdirectory()
    pathLable.config(text=location)

# loaction to save video
pathLable = Label(root,text="Select Location to save video: ")
canvas.create_window(250,130,window=pathLable)
pathButton = Button(root,text="Select",command=get_location)
canvas.create_window(250,160,window=pathButton)

# download video function
def downloadHRVideo():
    videoURL = urlEntry.get()
    location = pathLable.cget("text")
    video = YouTube(videoURL).streams.get_highest_resolution().download()
    videoClip = VideoFileClip(video)
    videoClip.close()
    shutil.move(video,location)
    print("high resolution video downloaded successfully")

# download video function
def downloadLRVideo():
    videoURL = urlEntry.get()
    location = pathLable.cget("text")
    video = YouTube(videoURL).streams.get_lowest_resolution().download()
    videoClip = VideoFileClip(video)
    videoClip.close()
    shutil.move(video,location)
    print("low resolution video downloaded successfully")

# download video
videoLable = Label(root,text="To Download video: ")
canvas.create_window(250,200,window=videoLable)
downloadButton = Button(root,text="Download High Resolution video", command=downloadHRVideo)
canvas.create_window(150,225,window=downloadButton)
downloadButton = Button(root,text="Download Low Resolution video", command=downloadLRVideo)
canvas.create_window(350,225,window=downloadButton)

# download adudio function
def downloadAudio():
    videoURL = urlEntry.get()
    location = pathLable.cget("text")
    video = YouTube(videoURL).streams.get_highest_resolution().download()
    videoClip = VideoFileClip(video)
    audio =  videoClip.audio
    audio.write_audiofile('audio.mp3')
    audio.close()
    shutil.move('audio.mp3',location)
    videoClip.close() 
    print("audio downloaded successfully")

# download audio
audioLable = Label(root,text="To Download Audio: ")
canvas.create_window(250,270,window=audioLable)
downloadButton = Button(root,text="Download audio",command=downloadAudio )
canvas.create_window(250,300,window=downloadButton)

root.mainloop()
