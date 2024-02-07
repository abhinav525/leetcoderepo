import tkinter as tk
from tkinter import *
win=tk.Tk()
win.title("KPIT")
lbl=Label(win,text="Welcome to Tkinter",fg="red",font=("Arial,22")) # it is the part of your window
lbl.place(x=60,y=50) # to place the label in  the window
win.geometry("500x600+10+20")
win.mainloop()
