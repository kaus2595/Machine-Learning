import pandas as pd
import matplotlib.pyplot as plt


#Reading Data
data = pd.read_csv("health.csv")
print(data.shape)

incr = 0
issue = list()
evaluation = list()
disease = list(data['HEALTH ISSUE'])
disease_csv = data['HEALTH ISSUE']
disease_count = dict()

for i in range(len(disease)):
    disease[i] = str(disease[i]).lower().strip()
    if (disease[i] == 'none' or disease[i] == 'nil' or disease[i] == 'no issues' or disease[i] == 'nothing'):
        disease[i] = 'none'

for i in range(len(disease_csv)):
    if(disease_csv[i] not in issue):
        issue.append(disease_csv[i])

for i in range(len(issue)):
    issue[i] = str(issue[i]).lower().strip()
    if(issue[i] == 'none' or issue[i] == 'nil' or issue[i] == 'no issues' or issue[i] == 'nothing'):
        issue[i] = 'none'


for i in range(len(issue)):
    for j in range(len(disease)):
        if(issue[i] == disease[j]):
            incr = incr+1
    evaluation.append(incr)
    incr = 0


disease_count = dict(zip(issue,evaluation))
print(disease_count)

#print(issue)
#print(evaluation)

plt.pie(disease_count.values(), labels=disease_count.keys(), startangle=90, autopct='%.0f%%')
plt.title('Disease V/S Count')
plt.show()
