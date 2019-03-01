from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("regression.csv")

x = data['X']
y = data['Y']
n = len(x)

x = x.reshape(n,1)
reg = LinearRegression()
reg = reg.fit(x,y)

plt.plot(x,y,color='#58b970', label="Regression Line")
plt.scatter(x,y, c="#ef5423", label = "Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
y_pred = reg.predict(x)
print(y_pred)
r2_score = reg.score(x,y)
print(r2_score)
plt.show()