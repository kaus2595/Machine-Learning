import pandas as pd

company = (pd.Series(['Google', 'Microsoft', 'GitHub', 'Adobe', 'Amazon']))
type = pd.Series(['Internet', 'Windows','Open Source','Software','Cloud'])

table = pd.DataFrame({"Comapany": company, "Bussiness":type})
print(table)