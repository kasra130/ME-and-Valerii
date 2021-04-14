from tkinter import *
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

    

def windowcolor():    #screen (inside) color
    root.configure(bg='black')      #black color


windowsize()
windowtitle()
windowcolor()




root.mainloop()