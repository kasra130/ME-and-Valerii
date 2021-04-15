import pandas as pd
class this:
    def __init__(self)
      
       self.csv_file_path = fd.askopenfilename(title="select a CSV file",filetypes=(("csv files", "*.csv"),)) #only csv accepted
       return self.csv_file_path
       v=csv_file_path
       Mydata = pd.read_csv(v)
       Mydata = Mydata.dropna()
       Mydata.head()

