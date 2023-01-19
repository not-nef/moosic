import tkinter
import sv_ttk
from tkinter import ttk, filedialog
from pygame import mixer
import os

nowplaying = ""

mixer.init()

root = tkinter.Tk()
root.title("Moosic")
root.geometry("300x150")
root.resizable(False, False)
sv_ttk.set_theme("dark")

next_light = tkinter.PhotoImage(file="assets/next_dark.png")
next_dark = tkinter.PhotoImage(file="assets/next_light.png")
pause_light = tkinter.PhotoImage(file="assets/pause_dark.png")
pause_dark = tkinter.PhotoImage(file="assets/pause_light.png")
play_light = tkinter.PhotoImage(file="assets/play_dark.png")
play_dark = tkinter.PhotoImage(file="assets/play_light.png")
previous_light = tkinter.PhotoImage(file="assets/previous_dark.png")
previous_dark = tkinter.PhotoImage(file="assets/previous_light.png")

def playsong():
    global nowplaying
    file = filedialog.askopenfilename()
    mixer.music.load(file)
    mixer.music.play()
    nowplaying = file
    lbl.configure(text="Now Playing: {}".format(nowplaying.split("/")[-1].split(".")[0]))

def refresh():
    if mixer.music.get_busy():
        btn1.configure(image=eval("pause_" + sv_ttk.get_theme()))
    else:
        btn1.configure(image=eval("play_" + sv_ttk.get_theme()))

    root.after(1000, refresh)

def playpause():
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        mixer.music.unpause()
        if not mixer.music.get_busy():
            mixer.music.play()

    refresh()

def previoussong():
    global nowplaying, file
    currentdir = os.listdir(nowplaying.removesuffix("/" + nowplaying.split("/")[-1]))
    def findprevious():
        global file, nowplaying
        file = nowplaying.removesuffix(nowplaying.split("/")[-1]) + currentdir[currentdir.index(nowplaying.split("/")[-1]) - 1]
        nowplaying = file
        if os.path.isdir(nowplaying):
            findprevious()
    findprevious()
    mixer.music.load(file)
    mixer.music.play()
    lbl.configure(text="Now Playing: {}".format(nowplaying.split("/")[-1].removesuffix("." + nowplaying.split(".")[-1])))


def nextsong():
    global nowplaying, file
    currentdir = os.listdir(nowplaying.removesuffix("/" + nowplaying.split("/")[-1]))
    def findnext():
        global file, nowplaying
        file = nowplaying.removesuffix(nowplaying.split("/")[-1]) + currentdir[currentdir.index(nowplaying.split("/")[-1]) + 1]
        nowplaying = file
        if os.path.isdir(nowplaying):
            findnext()
    findnext()
    mixer.music.load(file)
    mixer.music.play()
    lbl.configure(text="Now Playing: {}".format(nowplaying.split("/")[-1].removesuffix("." + nowplaying.split(".")[-1])))

btn = ttk.Button(root, text="Play song", command=playsong).pack()
btn1 = ttk.Button(root, command=playpause, image=eval("play_" + sv_ttk.get_theme()))
btn1.pack(pady=25)
lbl = tkinter.Label(root, text="Now Playing:")
lbl.pack()
btnprev = ttk.Button(root, command=previoussong, image=eval("previous_" + sv_ttk.get_theme()))
btnprev.place(x=50, y=57)
btnnext = ttk.Button(root, command=nextsong, image=eval("next_" + sv_ttk.get_theme()))
btnnext.place(x=199, y=57)

root.after(1000, refresh)
root.mainloop()