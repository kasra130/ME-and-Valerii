class Graph(self):                                     
        self.graph1location1= tk.Frame(frame2)     #frame
        self.graph1location1.place(x=10,y=180)     #location of graph
        fig = plt.figure(figsize=(7, 4), dpi=50,)  #creating an emty plot
        self.ax0 = fig.add_subplot(111)            #defined ax0
        self.chart1 = FigureCanvasTkAgg(fig, self.graph1location1)  #presented as chart
        self.chart1.get_tk_widget().pack()                          #pack() command for matching tkkinter
 
 
 
 

 #finding value for January
        self.ax0.set_title("KWH Jan 2010 bar"); self.ax0.set_xlabel(x); self.ax0.set_ylabel(y)
        Januarykwh = self.subdf.columns.get_loc('KWH JANUARY 2010')     #find the column   
        self.ax0.bar(range(1, 13), (self.subdf.iloc[:, range(Januarykwh, (Januarykwh+12))]) #getting the mean
