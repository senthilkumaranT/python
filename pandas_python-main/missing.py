import pandas as pd

data = pd.read_excel("/content/missing .xlsx")
data

new=data.fillna(0)
new


new_df= data.fillna(method="ffill")
new_df

new_d = data.interpolate()
new_d


drop= data.dropna()
drop


drop_1=data.dropna(thresh= 1)
drop_1


