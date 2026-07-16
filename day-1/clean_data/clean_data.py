import pandas as pd
import numpy as np

data = {
    'Customer': ['John', 'Sarah', 'Mike', 'Emily', 'David', 'Anna', 'Tom'],
    'Age': [28, '34', 22, '29', '41', 35, None],
    'City': ['New York', 'Chicago', 'new york', 'CHICAGO', 'Boston', 'Chicago', 'New York'],
    'Purchase_Amount': [150, 200, None, 300, 120, 180, 250],
    'Items_Bought': [3, 5, 2, 7, 4, '3', 6],
    'Join_Date': ['2023-01-15', '2023/02/20', '15-03-2023', '2023-04-10', '2023-05-05', '2023-06-01', '2023-07-12']
}

df = pd.DataFrame(data)

# replace all None/NaN with 0
df.fillna(0, inplace=True)

df = df.astype({ 'Age': int, 'Items_Bought': int })

df['Age'] = df['Age'].replace(0, df['Age'].mean())
df['Purchase_Amount'] = df['Purchase_Amount'].replace(0, df['Purchase_Amount'].median())

df['City'] = df['City'].str.lower().str.capitalize()
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

df['Total_Spend'] = df['Purchase_Amount'] * df['Items_Bought']


print("Customers from Chicago who spent > $150 🤩🕺\n")
print( df[ (df['City'] == 'Chicago') & (df['Total_Spend'] > 150) ] )

print("\n----------\nAll Customers:\n")

print( df.sort_values('Join_Date', ascending=True) )
