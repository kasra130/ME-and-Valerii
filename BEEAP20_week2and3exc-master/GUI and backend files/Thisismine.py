from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import tkinter.font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Prog:
    def __init__(self, root):
        root.title("Casper and valerii's app")    #changes the title of the window
        root.geometry("900x700")                  #size
        root.iconbitmap(r'BEEAP20_week2and3exc-master\image\favicon.ico')    #changed icon 
        root.configure(bg="black")                #screen to black
        root.resizable(width=False, height=False)   #disabling resizing for consistant presentation 
        frame1 =tk.LabelFrame(root, text="Data analyzer", fg="white", bg="black",font=("Times",20)).place(width=900, height=170)  #title on the screen
        frame2= tk.Frame(root, bg="black").place(x=3, y=180, width=900, height=530)
        info = "This program is desgined to only read *.csv files\nPlease select the file and choose the desired header from the combo box" #varible for help button 
        self.Cbutton=Button(root, text="Select File...",command=self.Ccommand).place(x=30, y=90, width=80, height=25)     #choose file button, its command has been called from the backend class (FANCCYYYY)
        self.Lbutton=Button(root, text="Graph").place(x=120, y=90, width=80, height=25) 
        self.exitbutton=Button(root, text="Exit", command=exit).place(x=3, y=660, width=60, height=25) #exit button
        self.helpbutton=Button(root, text="Help", command= lambda: ms.showinfo("Information",info)).place(x=840,y=30, width=60, height=25)   #help button
        

        
            
            #dropdown menu(combobox)


      
        self.dropdown = ttk.Combobox(root)                            #dropdown menu
        self.dropdown.place(x=600, y=90, width=200, height=25)        #place
        self.dropdown.bind("<<ComboboxSelected>>", self.comboBoxcity) #connection to csv
      
      

       

        
        






        #First graph

        self.graph1location1= tk.Frame(frame2)
        self.graph1location1.place(x=10,y=180)
        fig = plt.figure(figsize=(7, 4), dpi=50)
        self.ax1 = fig.add_subplot(111)
        self.chart1 = FigureCanvasTkAgg(fig, self.graph1location1)
        self.chart1.get_tk_widget().pack()
        
         
        #second graph     
        self.graph1location2= tk.Frame(frame2)
        self.graph1location2.place(x=540,y=180)
        fig = plt.figure(figsize=(7, 4), dpi=50)
        self.ax2 = fig.add_subplot(111)
        self.chart2 = FigureCanvasTkAgg(fig, self.graph1location2)
        self.chart2.get_tk_widget().pack()




        #third graph     
        self.graph1location3= tk.Frame(frame2)
        self.graph1location3.place(x=10,y=430)
        fig = plt.figure(figsize=(7, 4), dpi=50)
        self.ax3 = fig.add_subplot(111)
        self.chart3 = FigureCanvasTkAgg(fig, self.graph1location3)
        self.chart3.get_tk_widget().pack()





        #forth graph     
        self.graph1location4= tk.Frame(frame2)
        self.graph1location4.place(x=540,y=430)
        fig = plt.figure(figsize=(7, 4), dpi=50)
        self.ax4 = fig.add_subplot(111)
        self.chart4 = FigureCanvasTkAgg(fig, self.graph1location4)
        self.chart4.get_tk_widget().pack()




















       # self.__GLineEdit_517 = tk.Canvas(root)
        #self.__GLineEdit_517.place(x=50, y=130, width=234, height=140)

        #self.__GLineEdit_985 = tk.Canvas(root)
        #self.__GLineEdit_985.place(x=30, y=450, width=300, height=200) #dfbrfdgrtdb
    

        #self.__GLineEdit_700 = tk.Canvas(root)
        #self.__GLineEdit_700.place(x=310, y=290, width=234, height=158)

    def Ccommand(self):
        filePath = fd.askopenfilename(title="select a CSV file",filetypes=(("csv files", "*.csv"),)) #only csv accepted
        
        try:
             excel_filename = r"{}".format(filePath)
             self.df = pd.read_csv(excel_filename)
             self.dropdown['values']=list(self.df['COMMUNITY AREA NAME'].unique())
       
        except ValueError:
             tk.messagebox.showerror("Information", "The file you have chosen is invalid")
             return None
        except FileNotFoundError:
             tk.messagebox.showerror("Information", f"No such file as {file_path}")
             return None  
        Label(root,text="File location").place(x=20, y=130, width=300, height=20)     
        label_file=Label(root,text=excel_filename).place(x=20, y=150, width=300, height=20)   # needs to be considered


    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def comboBoxcity(self, event=None):
        self.subdf = self.df.loc[self.df['COMMUNITY AREA NAME'] == self.dropdown.get()]






if __name__ == "__main__":
    root = tk.Tk()
    program = Prog(root)
    root.mainloop()
