import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales_dat = pd.read_csv('./Sample Sales Data/sales_data_sample.csv',encoding='windows-1252')
sales_df1 = pd.DataFrame(sales_dat).iloc[:,:10]

# Plotting Sales Per Year Chart
# sales_df1.groupby('YEAR_ID')['SALES'].sum().plot(
#     kind='bar',figsize=(10,15),width=0.6,color='green',xlabel='Year',ylabel='Sales')
# plt.show()


# Plotting Sales of Product by Types 
sales_dat.groupby('PRODUCTLINE')['SALES'].sum().plot(kind='bar',width=0.5,figsize=(10,15),color='red',title='Sales of Product by Types',rot=0)
plt.show()
