from ast import Delete, Str
from cProfile import label
from cmath import exp
from ctypes.wintypes import WORD
from logging import root
from msilib.schema import Font
from re import fullmatch
from telnetlib import SE
from tkinter.constants import END, LEFT
from tkinter import ANCHOR, BOTH, CENTER, GROOVE, INSERT, N, S, TOP, X, Button, Frame, Label, ttk
import tkinter.messagebox
import tkinter as tk

from turtle import back, left, right, width
from types import CellType
from typing import Text
from matplotlib.pyplot import fill

from matplotlib.sankey import RIGHT
from sqlalchemy import column
root = tk.Tk()
root.title("Calculator")
root.geometry("600x500")
root.resizable(0,0)

#insert box
label_insert = tk.Entry(root,background="light blue",fg = "#000000",font = ("Cambria Math", 20))
label_insert.pack(expand=True,fill=BOTH, anchor= CENTER)

def NumOut(number):
    label_insert.insert(tk.END,number)

def Ans():
    try:
        y = str(eval(label_insert.get()))
        label_insert.delete(0, tk.END)
        label_insert.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")
def clear():
	label_insert.delete(0, tk.END)


fOne = Frame(root, bg = "white")  
fOne.pack(expand = True, fill = "both")
fTwo = Frame(root, bg = "white")  
fTwo.pack(expand = True, fill = "both")
fThree = Frame(root, bg = "white")  
fThree.pack(expand = True, fill = "both") 
fFour = Frame(root,bg="white")
fFour.pack(expand= True,fill="both")
fFive = Frame(root,bg="white")
fFive.pack(expand=False, fill=BOTH)
# frame can expand if it gets some space  
#button frameone
btn1 = Button(fOne,text="1",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(1),relief=GROOVE)
btn1.pack(side=LEFT,expand=True,fill=BOTH)
btn2 = Button(fOne,text="2",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(2),relief=GROOVE)
btn2.pack(side=LEFT,expand=True,fill=BOTH)
btn3 = Button(fOne,text="3",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(3),relief=GROOVE)
btn3.pack(side=LEFT,expand=True,fill=BOTH)
#button frametwo
btn1 = Button(fTwo,text="4",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(4))
btn1.pack(side=LEFT,expand=True,fill=BOTH)
btn2 = Button(fTwo,text="5",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(5))
btn2.pack(side=LEFT,expand=True,fill=BOTH)
btn3 = Button(fTwo,text="6",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(6))
btn3.pack(side=LEFT,expand=True,fill=BOTH)
#button framethree
btn1 = Button(fThree,text="7",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(7))
btn1.pack(side=LEFT,expand=True,fill=BOTH)
btn2 = Button(fThree,text="8",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(8))
btn2.pack(side=LEFT,expand=True,fill=BOTH)
btn3 = Button(fThree,text="9",font = ("Cambria", 22),border=0.2,command=lambda:NumOut(9))
btn3.pack(side=LEFT,expand=True,fill=BOTH)
#button framefour
btnDivine = Button(fFour,text="/",border=0.2,font = ("Cambria", 22),command=lambda: NumOut('/'))
btnDivine.pack(side=LEFT,expand=True,fill=BOTH)
btnAdd = Button(fFour,text="+",border=0.2,font = ("Cambria", 22),command=lambda: NumOut('+'))
btnAdd.pack(side=LEFT,expand=True,fill=BOTH)
btnMinus = Button(fFour,text="-",border=0.2,font = ("Cambria", 22),command=lambda: NumOut('-'))
btnMinus.pack(side=LEFT,expand=True,fill=BOTH)
btnMulti = Button(fFour,text="*",border=0.2,font = ("Cambria", 22),command=lambda: NumOut('*'))
btnMulti.pack(side=LEFT,expand=True,fill=BOTH)

btnAns = Button(fFour,text="=",border=0.2,font = ("Cambria", 22),command=Ans)
btnAns.pack(side=LEFT,expand=True,fill=BOTH)
btnClear = Button(fFour,text="Clear",border=0.2,font = ("Cambria", 22),command=clear)
btnClear.pack(side=LEFT,expand=True,fill=BOTH)

btnMode1 = Button(fFive,text="Mode 1",border=0.2,font=  ("Cambria, 22"))
btnMode1.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()