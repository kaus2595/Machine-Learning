from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

data = pd.read_csv("california_housing_train.csv")

x = data['population']
y = data['median_house_value']
n = len(x)

x = x.reshape(n,1)
reg = LinearRegression()
reg = reg.fit(x,y)

y_pred = reg.predict(x)

r2_score = reg.score(x,y)
print(r2_score)