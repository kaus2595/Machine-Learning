import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading Data
data = pd.read_csv("health.csv")
print(data.shape)
#print(data.head())

#Taking the columns from the dataset on which we have to work on
x = np.array()
print(x)
objects = data['HEALTH ISSUE']
for i in range(len(objects)):
    if(objects not in x):



print(objects)
y_pos = np.arange(len(objects))
print(type(y_pos))
performance = data['Count'][53:65]
print(type(performance))

#Plotting the graph between x and y
"""plt.bar(y_pos,performance,align="center",color='#58b970')
plt.xticks(y_pos,objects)
plt.xlabel("AGE")
#plt.ylabel("HEALTH ISSUE")
plt.show()"""