from cProfile import label
from codeop import CommandCompiler
from ctypes.wintypes import WORD
from distutils.cmd import Command
from logging import root
from msilib.schema import ComboBox, Font
from pydoc import plain
from secrets import choice
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

def exitProgram():
        confirm = tkinter.messagebox.askquestion("ok","do you want to exit")
        if confirm == "yes":
            root.destroy()

def showmessage():
    print("Test")

def aboutProgram():
    tkinter.messagebox.showinfo("info","python NaN")

def openTest():
    myWindow = tk.Tk()
    myWindow.title("test")
    myWindow.geometry("200x200")

def displayText():
    showtext = (txt.get())
    show_message.delete(0, END)
    show_message.insert(0, showtext)

def openText():
    myWindow = tk.Tk()
    myWindow.title("test")
    myWindow.geometry("200x200")

txt =  tk.StringVar()
txt2 =  tk.StringVar()

myText =tk.Entry(textvariable=txt, bg ="pink")
myText.place(x=300,y=150)
show_message = tk.Entry(textvariable=txt2, bg="light blue")
show_message.place(x=300,y=200)

label_insert = tk.Label(root,text="insert text",font=('calviri',10))
label_insert.place(x=300,y=120)
label_display = tk.Label(root,text="show text",font=('calviri',10))
label_display.place(x=300,y=175)

btn1 = tk.Button(root,text="show text", fg="red", bg="light blue",font="console 10", command=displayText).place(x=300,y=250)
btn2 = tk.Button(root,text="new window", fg="blue", bg="light blue",font="console 10", command=openText).place(x=300,y=300)

subMenu = tk.Menu()
subMenu.add_command(label="new file", command=openTest)
subMenu.add_command(label="save")
subMenu.add_command(label="exist", command=exitProgram)
subMenu.add_command(label="about",command=aboutProgram)

#readio button
def shoChoice():
    print(lang.get())


lang = tk.IntVar()
lang.set(1)
tk.Radiobutton(text="python",variable=lang, value=1, command=shoChoice).place(x=100,y=100)
tk.Radiobutton(text="c#",variable=lang, value=2, command=shoChoice).place(x=100,y=150)
tk.Radiobutton(text="java",variable=lang, value=3, command=shoChoice).place(x=100,y=200)
tk.Radiobutton(text="php",variable=lang, value=4, command=shoChoice).place(x=100,y=250)

def checkBtn():
    print(lang1.get(),lang2.get(),lang3.get(),lang4.get())

lang1 = tk.IntVar()
lang2 = tk.IntVar()
lang3 = tk.IntVar()
lang4 = tk.IntVar()
tk.Checkbutton(text="python",variable=lang1,command=checkBtn).place(x=200,y=150)
tk.Checkbutton(text="C#",variable=lang2,command=checkBtn).place(x=200,y=200)
tk.Checkbutton(text="Java",variable=lang3,command=checkBtn).place(x=200,y=250)
tk.Checkbutton(text="Php",variable=lang4,command=checkBtn).place(x=200,y=300)

def selectCity():
    Label(text="ur choice = " +choice.get()).place(x=250,y=10)
    pass 

choice = tk.StringVar(value="choose somethings")

combo =ttk.Combobox(textvariable=choice)
combo["value"]=("t1","t2","t3","t4")
combo.place(x=250,y=50)
btn3 = Button(text="show text in combobox",command = selectCity,width=20,height=3).place(x=80,y=20)
root.mainloop()