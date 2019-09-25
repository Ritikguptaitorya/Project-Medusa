import vlc
import time
import io
from tkinter import *
from tinytag import TinyTag, TinyTagException
from PIL import Image, ImageTk


def play():
    sound_file.play()
    # change to \ for windows
    temp_track = TinyTag.get("Music/01 - Drake - Jumpman.mp3", image=True)
    print("Now Playing:", temp_track.title)
    pic = temp_track.get_image()
    f1 = open("temp.jpg", "wb")
    f2 = f1.write(pic)
    img = ImageTk.PhotoImage(Image.open("temp.jpg"))

def pause():
    sound_file.pause()
    print("Stoped")


sound_file = vlc.MediaPlayer("Music/01 - Drake - Jumpman.mp3")
root = Tk()
root.title("Medusa")
root.geometry("300x400")
img = Image.open("temp.jpg")
img = img.resize((300,300), Image.ANTIALIAS)
img.save("temp.jpg")
img = ImageTk.PhotoImage(Image.open("temp.jpg"))
lpic = Label(root,image=img)
BtPlay = Button(root, text="Play", command=play)
BtPause = Button(root, text="Stop", command=pause)
lpic.grid(row=1,column=1)
BtPlay.grid(row=2,column=1)
BtPause.grid(row=3,column=1)
root.mainloop()
