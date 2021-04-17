class Graph(self):
        self.graph1location1= tk.Frame(frame2)     #frame
        self.graph1location1.place(x=200,y=500)     #location of graph
        fig = plt.figure(figsize=(10, 5), dpi=100,)  #creating an emty plot
        self.ax = fig.add_subplot(111)            #defined as ax0
        self.chart = FigureCanvasTkAgg(fig, self.graph1location1)  #presented as chart
        self.chart.get_tk_widget().pack()                          #pack() command for matching with tkkinter        




           #finding value for January
        self.ax0.set_title("KWH Jan 2010 bar"); self.ax0.set_xlabel(x); self.ax0.set_ylabel(y)
        Januarykwh = self.subdf.columns.get_loc['KWH JANUARY 2010']     #find the  column   
        self.ax0.bar( (self.subdf.iloc[:, range(Januarykwh, (Januarykwh+12)]).mean())   # getting the mean  

