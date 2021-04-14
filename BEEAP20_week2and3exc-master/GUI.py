from tkinter import *
from tkinter import filedialog as fd


root = Tk()
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
    root.iconbitmap(r'C:\Users\caspe\Desktop\Git test\ME-and-Volerii\BEEAP20_week2and3exc-master\image\favicon.ico')  #icon image 

    

def windowfeatures():    #screen (inside) color
    root.configure(bg='black')      #black color
    Label(root, text="Data analyzer", fg="white", bg="black",font=("Times",20)).grid(row=1, column=1)


def openfile():   #command
    return fd.askopenfilename()   # definig the open file command for the button 

def Pbutton():       #button for open gile 
    Button(root, text="Open file...", command=openfile).place(x=100, y=150, width=80, height=25)  #resizing button, and giving it a position, text and action command 
    Button(root, text="Exit", command=exit).place(x=20,y=350, width=60, height=25)

def comboboxx():
    ttk.combobox(root, text="hey").place(x=300, y= 150 , width=200, height=25)



windowsize()
windowtitle()
windowfeatures()
Pbutton()




root.mainloop()