# import csv

# with open('employees.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     data = [row for row in reader]
#     i=0
#     for row in data:
#         if(i==0):
#             continue
#         elif(i==1):
#             data.update({row[0]: row[i]})  
#         i+=1
# print(data)


import pandas as pd

df = pd.read_csv('employees.csv')
print(df)

data = df.to_dict(orient='records')
print(data)