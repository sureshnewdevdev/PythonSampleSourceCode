
# Import pandas
import pandas as pd

s = pd.Series([1, 2, 3, 4])
print(s)

data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data)

print('DataFrame:')
print(df)

df = pd.read_csv('customers-100.csv')

print('DataFrame loaded from CSV:')
print(df)

print('First 5 rows of the DataFrame:')
print(df.head(5))

print('Last 5 rows of the DataFrame:')
print(df.tail(5))

print('DataFrame Info:')
print(df.info())


df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])

print('DataFrame with custom columns:')
print(df)