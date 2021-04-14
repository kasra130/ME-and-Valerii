from tkinter import *
from tkinter import filedialog as fd
<<<<<<< Updated upstream
#from tkinter import tkk

root=Tk()
=======
from tkinter import messagebox as ms
import csv
import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
>>>>>>> Stashed changes

def windowsize():                                   #window size
    width = 500    #defining a standing width and height 
    height = 400 
    screenwidth = root.winfo_screenwidth()    #getting the screen size (width and height)
    screenheight = root.winfo_screenheight()
    centerx = '%dx%d+%d+%d' % (width, height,
        (screenwidth - width) / 2, (screenheight - height) / 2)   # opening the window in the middle of the screen (with respect to the screen size)
    root.geometry(centerx)  #call


def windowtitle():                  #window title and icon
    root.title("casper and valeeri's program")     #title
    root.iconbitmap(r'C:\Users\caspe\Desktop\Git test\ME-and-Volerii\BEEAP20_week2and3exc-master\images\favicon.ico')  #icon image 

    

def windowfeatures():    #screen (inside) color
    root.configure(bg='black')      #black color
    Label(root, text="Data analyzer", fg="white", bg="black",font=("Times",20)).grid(row=1, column=1)


<<<<<<< Updated upstream
def openfile():   #command
    return fd.askopenfilename()   # definig the open file command for the button 

def Pbutton():       #button for open gile 
    Button(root, text="Open file...", command=openfile).place(x=30, y=70, width=80, height=25)  #resizing button, and giving it a position, text and action command 
    Button(root, text="Exit", command=exit).place(x=20,y=350, width=60, height=25)
=======
def openfile():
    global v
    csv_file_path = fd.askopenfilename()
    v.set(csv_file_path)
    Data = v
    data = data.dropna()
    data.head()
    intocombo == data[data['COMMUNITY AREA NAME']]


def Pbutton():       #button for open gile 
    info = "This program is desgined to only read *.csv files\nPlease select the file and choose the desired header from the combo box"
    Button(root, text="Open file...", command=openfile).place(x=50, y=100, width=80, height=25)  #resizing button, and giving it a position, text and action command 
    Button(root, text="Exit", command=exit).place(x=1, y=650, width=60, height=25)  #exit button
    Button(root, text="Help", command=lambda:  ms.showinfo("Information",info)).place(x=830,y=10, width=60, height=25)    #help button
    

    
>>>>>>> Stashed changes


v = tk.StringVar()
OptionMenu(root, v, openfile).place(x=200, y=300, width=60, height=25)


<<<<<<< Updated upstream
=======

 

>>>>>>> Stashed changes




windowsize()
windowtitle()
windowfeatures()
Pbutton()



root.mainloop()