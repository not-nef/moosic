import tkinter
import sv_ttk
from tkinter import ttk, filedialog
from pygame import mixer
import pathlib

mixer.init()

root = tkinter.Tk()
root.title("Moosic")
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
    mixer.music.load(str(pathlib.Path(filedialog.askopenfilename())))
    mixer.music.play()

def updateicon():
    if mixer.music.get_busy():
        btn1.configure(image=eval("pause_" + sv_ttk.get_theme()))
    else:
        btn1.configure(image=eval("play_" + sv_ttk.get_theme()))

    root.after(1000, updateicon)

def playpause():
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        mixer.music.unpause()

    updateicon()




btn = ttk.Button(root, text="Play song", command=playsong).pack()
btn1 = ttk.Button(root, command=playpause, image=eval("play_" + sv_ttk.get_theme()))
btn1.pack()
root.after(1000, updateicon)
root.mainloop()