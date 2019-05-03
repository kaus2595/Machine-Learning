import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading Data
data = pd.read_csv("health.csv")
print(data.shape)

incr = 0
disease = list()
count_disease = list()
disease_city = list(data['CITY'])
disease_csv = data['CITY']

for i in range(len(disease_city)):
    disease_city[i] = str(disease_city[i]).lower().strip()
    if (disease_city[i] == 'none' or disease_city[i] == 'nil' or disease_city[i] == 'no issues' or disease_city[i] == 'nothing'):
        disease_city[i] = 'none'

for i in range(len(disease_csv)):
    if(disease_csv[i] not in disease):
        disease.append(disease_csv[i])


for i in range(len(disease)):
    disease[i] = str(disease[i]).lower().strip()
    if(disease[i] == 'none' or disease[i] == 'nil' or disease[i] == 'no issues' or disease[i] == 'nothing'):
        disease[i] = 'none'

for i in range(len(disease)):
    for j in range(len(disease_city)):
        if(disease[i] == disease_city[j]):
            incr = incr+1
    count_disease.append(incr)
    incr = 0



#Taking the columns from the dataset on which we have to work on
objects = disease
y_pos = np.arange(len(objects))
performance = count_disease

#Plotting the graph between x and y
plt.bar(y_pos,performance,color='#58b970')
plt.xticks(y_pos,objects)
plt.xlabel("AREA")
#plt.ylabel("HEALTH ISSUE")
plt.show()