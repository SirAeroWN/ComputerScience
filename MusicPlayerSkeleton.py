import pygame
from tkinter import *

def playsong():
    pygame.mixer.music.play()

def pausesong():
    pygame.mixer.music.pause()

def unpausesong():
    pygame.mixer.music.unpause()

def stopsong():
    pygame.mixer.music.stop()
    
pygame.mixer.init()
songfile = 'songs/Peaches.mp3'
pygame.mixer.music.load(songfile)
root =Tk()
root.title('entry widget')
Button(root, text='Play', command = playsong).pack(side= LEFT)
Button(root, text='Pause', command = pausesong).pack(side= LEFT)
Button(root, text='Unpause', command = unpausesong).pack(side= LEFT)
Button(root, text='Stop', command = stopsong).pack(side= RIGHT)


root.mainloop()





