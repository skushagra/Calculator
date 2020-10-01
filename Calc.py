import tkinter 
from tkinter import *
from tkinter import messagebox
import math

root = tkinter.Tk()
root.geometry("600x600+300+300")
#root.resizable()
frm1 = Frame(root, bg = "#000000")
frm1.pack(expand=True, fill="both",)
frm2 = Frame(root, bg = "#ffffff")
frm2.pack(expand=True, fill="both",)




def modebasic():
      import Calculator
def modesci():
      pass






btn1=Button(frm1,
            text="Basic Mode",
            font = ("Fira Code Light", 22),
	     bg = "#000000", 
            fg="#ffffff",
            command = modebasic).pack(expand=True,fill="both")
btn2=Button(frm2, 
            text="Scientific Mode", 
            font = ("Fira Code Light", 22), 
            bg = "#ffffff",
            fg="#000000",
            command = modesci).pack(expand=True,fill="both")
root.mainloop()
