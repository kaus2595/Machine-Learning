import numpy as np
#from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

#plt.rcParams['figure.figsize'] = (20.0,10.0)


#Reading Data
data = pd.read_csv("california_housing_train.csv")
print(data.shape)
#print(data.head())

#random_indices = np.random.permutation(data)
x = data['population']
y = data['median_house_value']

mean_x = np.mean(x)
mean_y = np.mean(y)

n = len(x)

numer = 0
deno = 0
for i in range(n):
    numer += (x[i]-mean_x) * (y[i] - mean_y)
    deno += (x[i]-mean_x) ** 2

b1 = numer/deno
b0 = mean_y - (b1* mean_x)

print(b1,b0)

max_x = np.max(x) + 100
min_x = np.min(x) - 100

x = np.linspace(min_x, max_x, 1000)
y = b0+b1*x

plt.plot(x,y,color='#58b970', label="Regression Line")
plt.scatter(x,y, c="#ef5423", label = "Scatter Plot")

plt.xlabel("Population")
plt.ylabel("Median House Value")
plt.legend()
plt.show()