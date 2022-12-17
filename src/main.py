import tkinter
import sv_ttk
from tkinter import ttk, filedialog
from pygame import mixer
import pathlib

mixer.init()

paused = True

root = tkinter.Tk()
root.title("Moosic")
sv_ttk.set_theme("light")

def playsong():
    global paused
    filepath = filedialog.askopenfilename()

    mixer.music.load(str(pathlib.Path(filepath)))
    mixer.music.play()

    paused = False

def playpause():
    global paused

    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True



btn = ttk.Button(root, text="Play song", command=playsong).pack()
btn1 = ttk.Button(root, text="Play / Pause", command=playpause).pack()
root.mainloop()