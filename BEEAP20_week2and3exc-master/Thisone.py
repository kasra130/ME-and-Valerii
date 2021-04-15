from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import csv
import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
root=Tk()

class window:
    def __init__(self, root, title, geometry, icon,bg):
        self.root = root     #root
        self.root.title(title)         #define title
        self.root.geometry(geometry)   #define size(wxh)
        self.root.iconbitmap(icon)     #window icon
        self.root.configure(bg="black")#preset color to black coz we are goths  
        root.resizable(width=False, height=False)   #disabling resizing for consistant presentation 
<<<<<<< Updated upstream:BEEAP20_week2and3exc-master/window.py
<<<<<<< Updated upstream
        self.heading=Label(self.root, text="Data analyzer", fg="white", bg="black",font=("Times",20)).grid(row=1, column=1)  #title on the screen


        info = "This program is desgined to only read *.csv files\nPlease select the file and choose the desired header from the combo box" #varible used 
        self.Cbutton=Button(self.root, text="Select File...",command= lambda: Backend.openfile(self)).place(x=30, y=90, width=80, height=25)        #choose file button, its command has been called from the backend class (FANCCYYYY)
        self.exitbutton=Button(self.root, text="Exit", command=exit).place(x=3, y=660, width=60, height=25) #exit button
        self.helpbutton=Button(self.root, text="Help", command= lambda: ms.showinfo("Information",info)).place(x=830,y=10, width=60, height=25)
          
=======
=======
>>>>>>> Stashed changes:BEEAP20_week2and3exc-master/Thisone.py
        self.frame1 =LabelFrame(self.root, text="Data analyzer", fg="white", bg="black",font=("Times",20)).place(width=900, height=200)  #title on the screen


        info = "This program is desgined to only read *.csv files\nPlease select the file and choose the desired header from the combo box" #varible used 
        self.Cbutton=Button(self.root, text="Select File...",command= lambda: openfile()).place(x=30, y=90, width=80, height=25)        #choose file button, its command has been called from the backend class (FANCCYYYY)
        self.Lbutton=Button(self.root, text="Load File",command= lambda: Load_excel_data()).place(x=120, y=90, width=80, height=25) 
        self.exitbutton=Button(self.root, text="Exit", command=exit).place(x=3, y=660, width=60, height=25) #exit button
        self.helpbutton=Button(self.root, text="Help", command= lambda: ms.showinfo("Information",info)).place(x=840,y=30, width=60, height=25)
        
<<<<<<< Updated upstream:BEEAP20_week2and3exc-master/window.py
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes:BEEAP20_week2and3exc-master/Thisone.py



        self.combo=ttk.Combobox(root)
<<<<<<< Updated upstream:BEEAP20_week2and3exc-master/window.py
<<<<<<< Updated upstream
        self.combo.place(x=350, y=90, width=300, height=30)
        self.combo.bind("<<comboboxSelected>>",readnow)

=======
=======
>>>>>>> Stashed changes:BEEAP20_week2and3exc-master/Thisone.py
        self.combo.place(x=250, y=90, width=300, height=30)
        self.combo.bind("<<comboboxSelected>>",combo )#t


        
        
>>>>>>> Stashed changes

        self.root.mainloop()


          
         



<<<<<<< Updated upstream
class Backend:
    def __init__(self):
        pass
    @staticmethod
    def openfile(self):
        csv_file_path = fd.askopenfilename(title="select a CSV file",filetypes=(("csv files", "*.csv"),)) #only csv accepted
        return csv_file_path
=======
     
        
      
>>>>>>> Stashed changes
    
    def readingmethod(self):
        v=csv_file_path
        self.Mydata= pd.read_csv(v)
        self.Mydata=Mydata.dropna()
        self.Mydata.head()
        
        
    
label_file=Label(root,text="this").place(x=30, y=400, width=60, height=25)


 
def screen():
<<<<<<< Updated upstream:BEEAP20_week2and3exc-master/window.py
<<<<<<< Updated upstream
    window1=window(root,"casper and valeeri's program", "900x700", r'C:\Users\caspe\Desktop\Git test\ME-and-Volerii\BEEAP20_week2and3exc-master\image\favicon.ico',"black")

def readnow():
    Backend.readingmethod(self)
    self.Cities = self.Mydata.loc[self.Mydata['COMMUNITY AREA NAME']==self.combo.get()]
    print(self.Cities.head())


screen()

readnow()

=======
    window1=window(root,"casper and valeeri's program", "900x700", r'C:\Users\caspe\Desktop\Git test\ME-and-Volerii\BEEAP20_week2and3exc-master\images\favicon.ico',"black")
def openfile():
    name = fd.askopenfilename(title="select a CSV file",filetypes=(("csv files", "*.csv"),)) #only csv accepted
    label_file["text"]=name
    return None    

def Load_excel_data():
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        df = pd.read_csv(excel_filename)
       
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

def combo():
    df=df.dropna()
    df.head()
    drop=df.loc[df['COMMUNITY AREA NAME'] == window.combo.get()]
    print(drop)

screen()
#file_path = ttk.Label(root, text="No file selected").place(x=30, y=150)
>>>>>>> Stashed changes



=======
    window1=window(root,"casper and valeeri's program", "900x700", r'C:\Users\caspe\Desktop\Git test\ME-and-Volerii\BEEAP20_week2and3exc-master\images\favicon.ico',"black")
def openfile():
    name = fd.askopenfilename(title="select a CSV file",filetypes=(("csv files", "*.csv"),)) #only csv accepted
    label_file["text"]=name
    return None    

def Load_excel_data():
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        df = pd.read_csv(excel_filename)
       
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

def combo():
    df=df.dropna()
    df.head()
    drop=df.loc[df['COMMUNITY AREA NAME'] == window.combo.get()]
    print(drop)

screen()
#file_path = ttk.Label(root, text="No file selected").place(x=30, y=150)
>>>>>>> Stashed changes:BEEAP20_week2and3exc-master/Thisone.py
