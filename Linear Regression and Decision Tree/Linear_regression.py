import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading Data
data = pd.read_csv("california_housing_train.csv")
print(data.shape)
#print(data.head())

#Taking the columns from the dataset on which we have to work on
x = data['population']
y = data['median_house_value']

#Finding the mean of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)

#Finding the total length of the dataset
n = len(x)

numer = 0
deno = 0

#Iterating through each element in the dataset as there is summation to find the value of y
for i in range(n):
    numer += (x[i]-mean_x) * (y[i] - mean_y)
    deno += (x[i]-mean_x) ** 2

b1 = numer/deno
b0 = mean_y - (b1* mean_x)

print(b1,b0)

max_x = np.max(x) + 100
min_x = np.min(x) - 100

#Providing the linspace to the data
x = np.linspace(min_x, max_x, 1000)
y = b0+b1*x

#Plotting the graph between x and y
plt.plot(x,y,color='#58b970', label="Regression Line")
plt.scatter(x,y, c="#ef5423", label = "Scatter Plot")

plt.xlabel("Population")
plt.ylabel("Median House Value")
plt.legend()
plt.show()