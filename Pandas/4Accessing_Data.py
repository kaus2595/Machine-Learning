import pandas as pd

company = (pd.Series(['Google', 'Microsoft', 'GitHub', 'Adobe', 'Amazon'])) #List datatype
field = pd.Series(['Internet', 'Windows','Open Source','Software','Cloud'])

table = pd.DataFrame({"Company": company, "Bussiness":field}) #dictionary datatype
print(type(table['Company']))
print(table['Company'])

#Accessing value through index
print("Accessing throgh index")
print(type(table['Company'][3]))
print(table['Company'][2])

#Accessing through slicing
print("Accessing through slicing")
print(table['Company'][1:3])