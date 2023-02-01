from ctypes.wintypes import WORD
from logging import root
from msilib.schema import Font
from tkinter.constants import END, LEFT
from tkinter import TOP, X, Button, Label, ttk
import tkinter.messagebox

import tkinter as tk

from turtle import width
from typing import Text
from matplotlib.pyplot import fill

from matplotlib.sankey import RIGHT
from sqlalchemy import column
root = tk.Tk()
root.title("My GUI")
root.geometry("500x400")

def extProgram():
        confirm = tkinter.messagebox.askquestion("ok","do you want to exit")
        if confirm == "yes":
            root.destroy()

# mylabel = Label(root,text = "apple", fg = "red", bg = "blue").pack(side=TOP, fill=X, ipadx=10, ipady=10,padx=10,pady=10)
# mylabel = Label(root,text = "banana", fg = "red", bg = "blue").pack()
# mylabel = Label(root,text = "coconut", fg = "red", bg = "blue").pack()
# mylabel = Label(root,text = "tulip", fg = "red", bg = "blue").pack()

# กำหนดตำแหน่ง frame บน display
f1 = tk.Frame(root, bg="green")
f1.place(x=1,y=1)
f2 = tk.Frame(root, bg="grey")
f2.place(x=1,y=50)
f3 = tk.Frame(root, bg="blue")
f3.place(x=270,y=50)

# show things on frame
Label(f1, text="",width=68).pack(padx=10,pady=10)

for menu in ['moc','lat','esp','ame','cap']:
    Button(f2,text=menu, width=30).pack(fill=X,padx=20,pady=10)

for i, c in enumerate("123456789"):
    Button(f3,text=c, width=6, height=3).grid(row=i//3,column=i%3,padx=10,pady=10)

root.mainloop()


