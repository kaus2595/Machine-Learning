import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading Data
data = pd.read_csv("health.csv")
print(data.shape)
#print(data.head())

#Taking the columns from the dataset on which we have to work on
issue = data['HEALTH ISSUE'][67:]
evaluation = data['Count'][67:]
#print(y_number)
print(issue)
print(evaluation)
plt.pie(evaluation, labels=issue, startangle=90, autopct='%.1f%%')
plt.title('Delhi Disease Chart')
plt.show()