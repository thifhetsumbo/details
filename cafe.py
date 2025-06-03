# ************ Compulsory Task 1 ************

''' This program calculates the total worth of the stock 
in the cafe, from available stock and price for each 
item listed in the cafe's menu'''

# List items in the cafe's menu.

menu = ['Cappuccino', 'Muffin', 'Latte', 'Cookie', 'Americano', 'Scone']

# Give the stock value for each item in the menu.

stock = {'Cappuccino': 8,
         'Muffin': 6,
         'Latte': 5,
         'Cookie': 4,
         'Americano': 3,
         'Scone': 7}

# Give the price for each item in the menu.

price = {'Cappuccino': 38.54,
         'Muffin': 12.99,
         'Latte': 35.49,
         'Cookie': 8.99,
         'Americano': 32.99,
         'Scone': 5.25}

# Define stock value as a list.

stock_value = []

# Calculate value of each item in the menu.

for item in menu:
    item_value = stock[item] * price[item]

# Add each item value into a list.

    stock_value.append(item_value)

# Take the sum of all item values.

    total_stock = sum(stock_value)

# Display the total worth of the stock in the cafe. 

print(f"Total stock worth in the cafe: {total_stock:.2f}")
