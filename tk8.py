import tkinter as tk
from tkinter import *
win=tk.Tk()
win.title("KPIT")
win.geometry("600x500+10+20")
txt1=Entry(win,font=("Arial",28))
txt1.place(x=50,y=75)
txt2=Entry(win,font=("Arial",28))
txt2.place(x=50,y=150)
txt3=Entry(win,font=("Arial",28))
txt3.place(x=50,y=300)

def sum():
    var1=int(txt1.get())
    var2=int(txt2.get())
    var3=var1+var2
    txt3.delete(0,10)
    txt3.insert(INSERT,str(var3))

btn=Button(win,text="Add",command=sum,font=("Arial",16))
btn.place(x=150,y=225)

menu_bar=tk.Menu(win)
file_menu=tk.Menu(menu_bar,tearoff=0) # tearoff will be a line that comes under a menu bar
menu_bar.add_cascade(label="FILE",menu=file_menu)

#add menu items
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=win.quit)

win.config(menu=menu_bar)
win.mainloop()