from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import csv


root = Tk()

def windowsize():                                   #window size
    width = 900    #defining a standing width and height 
    height = 700 
    screenwidth = root.winfo_screenwidth()    #getting the screen size (width and height)
    screenheight = root.winfo_screenheight()
    centerx = '%dx%d+%d+%d' % (width, height,
        (screenwidth - width) / 2, (screenheight - height) / 2)   # opening the window in the middle of the screen (with respect to the screen size)
    root.geometry(centerx)  #call
    root.resizable(width=False, height=False)   #disabling resizing for consistant presentation 


def windowtitle():                  #window title and icon
    root.title("casper and valeeri's program")     #title
    root.iconbitmap(r'C:\Users\caspe\Desktop\Git test\ME-and-Volerii\BEEAP20_week2and3exc-master\image\favicon.ico')  #icon image 

    

def windowfeatures():    #screen (inside) color
    root.configure(bg='black')      #black color
    Label(root, text="Data analyzer", fg="white", bg="black",font=("Times",20)).grid(row=1, column=1)



def openfile():   #command
    thefile = fd.askopenfilename(title="select a file", filetypes=(("csv files","*.csv"),))   # definig the open file command for the button 
    return thefile

    print(len(thefile.name))
def Pbutton():       #button for open gile 
    info = "This program is desgined to only read *.csv files\nPlease select the file and choose the desired header from the combo box"
    Button(root, text="Open file...", command=openfile).place(x=50, y=100, width=80, height=25)  #resizing button, and giving it a position, text and action command 
    Button(root, text="Exit", command=exit).place(x=1, y=650, width=60, height=25)  #exit button
    Button(root, text="Help", command=lambda:  ms.showinfo("Information",info)).place(x=830,y=10, width=60, height=25)    #help button
    





    





windowsize()
windowtitle()
windowfeatures()
Pbutton()





root.mainloop()