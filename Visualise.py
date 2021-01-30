#imported matplotlib
import matplotlib.pyplot as plt

#Made barchart to confirm no missing data
data.isna().sum().plot(kind="bar")

#To show graph
#plt.show()

#To save the graph
#plt.savefig()

sns.set_style("whitegrid")

g= sns.relplot(x= "year",
            y= "AveragePrice",
            data= new_data,
            kind= "line",
            hue= "type",
            size= "type",
            ci= None)

g.fig.suptitle("Avacados by type and average cost")
g.set(xlabel="Year",
       ylabel="Average price")

plt.show()

sns.set_style("whitegrid")

g= sns.relplot(x= "year",
            y= "Total Volume",
            data= new_data,
            kind= "line",
            hue= "type",
            size= "type",
            ci= None)

g.fig.suptitle("Avacados by type and total volume")
g.set(xlabel="Year",
       ylabel="Total volume")

plt.show()