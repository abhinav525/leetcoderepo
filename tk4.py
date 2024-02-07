import tkinter as tk
from tkinter import * # * import all the library form the package
win=tk.Tk()
win.title("KPIT")
lal=Label(win,text="Welcome to tkinter",fg="blue",font=("Harlow Solid Italic",24))
txtfld=Entry(win)
txtfld.place(x=85,y=100)

btn=Button(win,text="Exit",command=quit,font=("arial",36)) #quick will close the window
lal.place(x=60,y=50)
btn.place(x=120,y=200)
win.geometry("600x500+10+20")
win.mainloop()