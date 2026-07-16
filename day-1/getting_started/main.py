import pandas as pd

data = {
    'Name': ['Omar', 'Ahmed', 'Ali', 'Osama', 'Marwan'],
    'Age': [28, 34, 25, 31, 21],
    'City': ['New York', 'Chicago', 'New York', 'Chicago', 'Boston'],
    'Purchase_Amount': [150, 200, 300, 90, 175],
    'Items_Bought': [1, 3, 4, 2, 6]
}

df = pd.DataFrame(data)

def get_city_df(df, city_name: str):
    return df[df['City'] == city_name]


def calc_city_average_price(df, city_name: str) -> float:
    df_city = get_city_df(city_name)
    return df_city['Average_Price'].mean()


print("All Customers from New York:")
print("============================")
print(get_city_df(df, 'New York'))

df['Average_Price'] = df['Purchase_Amount'] / df['Items_Bought']

calc_city_average_price(df, 'New York')

# Filter customers who spent 
# more than $100 AND bought more than 3 items

print("\nCustomers who spent > $100 AND bought > 3 items: 🫶")

vip_customers = df[ (df['Purchase_Amount'] > 100) & (df['Items_Bought'] > 3) ]
        
print(f"\n{vip_customers}")

# Sort the DataFrame by 
# Purchase_Amount (highest first)

print("\n", df.sort_values('Purchase_Amount', ascending=False) )

# Find the customer with
# the highest Average_Price

print("\nCustomer with the highest average price:\n")

print(df.sort_values('Average_Price', ascending=False).iloc[0])
