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
        root.iconbitmap(r'BEEAP20_week2and3exc-master\image\favicon.ico')    #change icon , You need to take relavant image path, if no possible just comment this out and it will run ...
        root.configure(bg="black")                #screen to black
        root.resizable(width=False, height=False)   #disabling resizing for consistant presentation 
        frame1 =tk.LabelFrame(root, text="Data analyzer", fg="white", bg="black",font=("Times",20)).place(width=900, height=170)  #title on the screen
        frame2= tk.Frame(root, bg="black").place(x=3, y=180, width=900, height=530)
        info = "This program is desgined to only read *.csv files\nPlease select the file and choose the desired header from the combo box\n This specific version can only read khoa's file" #varible for help button 
        self.Cbutton=Button(root, text="Select File...",command=self.Ccommand).place(x=30, y=90, width=80, height=25)     #choose file button
        self.exitbutton=Button(root, text="Exit", command=exit).place(x=3, y=660, width=60, height=25) #exit button
        self.helpbutton=Button(root, text="Help", command= lambda: ms.showinfo("Information",info)).place(x=840,y=30, width=60, height=25)   #help button
        

        
            
            #dropdown menu(combobox)


      
        self.dropdown = ttk.Combobox(root)                            #dropdown menu
        self.dropdown.place(x=600, y=90, width=200, height=25)        #place
        self.dropdown.bind("<<ComboboxSelected>>", self.comboBoxcity) #connection to csv
      
      

       

        
        






        #First graph

        self.graph1location1= tk.Frame(frame2)     #the below frame (fram22)
        self.graph1location1.place(x=10,y=180)     #position 
        fig = plt.figure(figsize=(7, 4), dpi=50,)  #plotting an empty 7x4 graph
        self.ax0 = fig.add_subplot(111)            #defined as ax0
        self.chart1 = FigureCanvasTkAgg(fig, self.graph1location1)  #presented as (canavas) chart
        self.chart1.get_tk_widget().pack()                          #pack() command for stuffing into tkkinter        repeated 4x
        
         
        #second graph     
        self.graph1location2= tk.Frame(frame2)
        self.graph1location2.place(x=540,y=180)
        fig = plt.figure(figsize=(7, 4), dpi=50)
        self.ax1 = fig.add_subplot(111)
        self.chart2 = FigureCanvasTkAgg(fig, self.graph1location2)
        self.chart2.get_tk_widget().pack()




        #third graph     
        self.graph1location3= tk.Frame(frame2)
        self.graph1location3.place(x=10,y=430)
        fig = plt.figure(figsize=(7, 4), dpi=50)
        self.ax2 = fig.add_subplot(111)
        self.chart3 = FigureCanvasTkAgg(fig, self.graph1location3)
        self.chart3.get_tk_widget().pack()





        #forth graph     
        self.graph1location4= tk.Frame(frame2)
        self.graph1location4.place(x=540,y=430)
        fig = plt.figure(figsize=(7, 4), dpi=50)
        self.ax3 = fig.add_subplot(111)
        self.chart4 = FigureCanvasTkAgg(fig, self.graph1location4)
        self.chart4.get_tk_widget().pack()















    def Ccommand(self):                                                                               #command for cbutton to choose a file 
        filePath = fd.askopenfilename(title="select a CSV file",filetypes=(("csv files", "*.csv"),))  #only .csv accepted
        
        try:
             excel_filename = r"{}".format(filePath)
             self.df = pd.read_csv(excel_filename)
             self.dropdown['values']=list(self.df['COMMUNITY AREA NAME'].unique())              #making sure that you have opened the specified file (error if no COMMUNITY NAME AREA)
       
        except ValueError:
             tk.messagebox.showerror("Information", "The file you have chosen is invalid")
             return None
        except FileNotFoundError:
             tk.messagebox.showerror("Information", f"No such file as {file_path}")
             return None  
        Label(root,text="File location").place(x=20, y=130, width=300, height=20)     
        label_file=Label(root,text=excel_filename).place(x=20, y=150, width=300, height=20)   #showing the file path 


    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def comboBoxcity(self, event=None):
        self.subdf = self.df.loc[self.df['COMMUNITY AREA NAME'] == self.dropdown.get()]     #will present all the .head() of the file into the combo box
       

        self.ax0.clear()      #getting rid of the orginially dummy plots (keeping thier size and attribute)
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        x="month in order"      #used to label x and y axis
        y="KWH"
        y2="THERM"
        
        #define january kwh information for graph1 
        self.ax0.set_title("KWH Jan 2010 bar"); self.ax0.set_xlabel(x); self.ax0.set_ylabel(y)
        Januarykwh = self.subdf.columns.get_loc('KWH JANUARY 2010')     #find the january column   
        self.ax0.bar(range(1, 13), (self.subdf.iloc[:, range(Januarykwh, (Januarykwh+12))]).mean())   #thanks to illia : getting the mean of the value,  



        #define January THERM information in graph 2                                                       
        self.ax1.set_title("THERM Jan 2010 bar"); self.ax1.set_xlabel(x); self.ax1.set_ylabel(y2)     #same but for therm
        JanuaryTHERM = self.subdf.columns.get_loc('THERM JANUARY 2010')
        self.ax1.bar(range(1, 13), (self.subdf.iloc[:, range(JanuaryTHERM, (JanuaryTHERM+12))]).mean())


        #define January KWH information in hist graph3                                                 #same but plot is used for line graph instead of bar 
        self.ax2.set_title("KWH Jan 2010 line graph"); self.ax2.set_xlabel(x); self.ax2.set_ylabel(y)
        Januarykwh = self.subdf.columns.get_loc('KWH JANUARY 2010') 
        self.ax2.plot(range(1, 13), (self.subdf.iloc[:, range(Januarykwh, (Januarykwh+12))]).mean())


        self.ax3.set_title("THERM Jan 2010 line graph"); self.ax3.set_xlabel(x); self.ax3.set_ylabel(y2)
        JanuaryTHERM = self.subdf.columns.get_loc('THERM JANUARY 2010')
        self.ax3.plot(range(1, 13), (self.subdf.iloc[:, range(JanuaryTHERM, (JanuaryTHERM+12))]).mean())



        







        self.chart1.draw()       #actuating the charts 
        self.chart2.draw()
        self.chart3.draw()
        self.chart4.draw()









if __name__ == "__main__":
    root = tk.Tk()
    program = Prog(root)
    root.mainloop()
