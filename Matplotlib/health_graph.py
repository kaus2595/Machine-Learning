import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading Data
data = pd.read_csv("health.csv")
print(data.shape)
#print(data.head())

#Taking the columns from the dataset on which we have to work on
x = data['HEALTH ISSUE']
y = data['AGE']

#Plotting the graph between x and y
plt.plot(x,y,color='#58b970')
#plt.scatter(x,y, c="#ef5423", label = "Scatter Plot")

plt.xlabel("AGE")
plt.ylabel("HEALTH ISSUE")
plt.legend()
plt.show()