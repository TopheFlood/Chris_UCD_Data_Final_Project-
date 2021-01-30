#imported matplotlib
import matplotlib.pyplot as plt

#Made barchart to confirm no missing data
data.isna().sum().plot(kind="bar")

#To show graph
#plt.show()

#To save the graph
#plt.savefig()
