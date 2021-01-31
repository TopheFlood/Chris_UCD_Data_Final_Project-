#print(data.sort_index())

#sorted data by region
data_sorted_region= (data.sort_index(level="region"))

#sliced using iloc to show the first 10 rows
print(data_sorted_region.iloc[0 : 10])

#used sort index on year
date_ind = data.set_index("year").sort_index()

#used loc to print years between 2015 and 2016
print(date_ind.loc["2015":"2016"])

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

#used drop duplicates to see the individual if every region had both types type
regions = data.drop_duplicates(subset = ["region" ,"type"])

print(regions.head())

#found total volume by type
volume_by_type = data.groupby("type")["Total Volume"].sum()

#printed data
print(volume_by_type)

#Created a for loop
for lab, row in data.iterrows():
    print(str(lab) + ": " + str(row["region"]))

 #Merging data frames - Not useful as all from one original data set but this is method
west_us_total_merge = total_us_volume.merge(total_west_volume, on= ["Date", "region"])