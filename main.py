import pandas as pd

data= pd.read_csv("avacados_data.csv")
#First look at data
print(data.head())

# to see the largest average price it was 3.25
print(data["AveragePrice"].max())

#checked for missing values
print(data.isna())

#checked by column
print(data.isna().any())

#imported matplotlib
import matplotlib.pyplot as plt

#Made barchart to confirm no missing data
data.isna().sum().plot(kind="bar")

#To show graph
plt.show()
#To save the graph
plt.savefig()




