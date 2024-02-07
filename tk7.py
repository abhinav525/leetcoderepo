import Tk.label as tk
from tkinter import *
import pygame
win=tk.Tk()
win.title("KPIT")
win.geometry("600x500")
pygame.mixer.init()

def play():
    pygame.mixer.music.load("")
    pygame.mixer.play(loops=0)

lbl=Label(win,text="music player",bd=9,relief=GROOVE,font=("Comic Sans",18),bg="white",fg="black")