import pandas as pd

data= pd.read_excel("/content/reshape.xlsx")
data


pd.melt(data,id_vars="date")


data1 = pd.melt(data, id_vars=["date"]) # Changed 'data' to 'date' in id_vars
data1[data1["variable"] == "temperature"] # Changed 'variable1' to 'variable'



