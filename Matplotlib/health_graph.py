import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading Data
data = pd.read_csv("health.csv")
print(data.shape)
#print(data.head())

#Taking the columns from the dataset on which we have to work on
objects = data['HEALTH ISSUE'][53:65]
y_pos = np.arange(len(objects))
performance = data['Count'][53:65]

#Plotting the graph between x and y
plt.bar(y_pos,performance,align="center",color='#58b970')
plt.xticks(y_pos,objects)
plt.xlabel("AGE")
#plt.ylabel("HEALTH ISSUE")
plt.show()