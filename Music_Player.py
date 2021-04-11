'''
It's a simple music player appliaction build using python 
It has various functionalities like:
1.choose a song from the play list 
2.play a song 
3.pause a song
4.unpause the song 
5.stop a song from playing and select another song from playist.
6.we can resize the application according to our need.
'''
'''
module included
=================
1. Pygame : for importing sounds libraries and computer graphics(its a module for creating video games) 
2. Tkinter : for application window using gui
  -> from Tkinter module we will import filedialogue : used for open and   save function.
  ->Askdirectory from filedialog : it provides a popup window to choose a directory from your window.
3. Os : for intracting with the os

features:
==========
1. create a application window
2. add a title to application window
3. set the size of the application window

Installation
=============
pygame doesnt come with python installation we have to install it seperately.
  in terminal 
  pip install pygame
'''

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x450")

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold",
                       bg="pink", selectmode=tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos+1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def ExitMusicPlayer():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


Button1 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="PLAY", command=play, bg="purple", fg="white")

Button2 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="STOP", command=ExitMusicPlayer, bg="dark blue", fg="white")

Button3 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="PAUSE", command=pause, bg="dark green", fg="white")

Button4 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     text="UNPAUSE", command=unpause, bg="brown", fg="white")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()
