menu = ["Cupcakes", "Muffins", "Sandwiches", "Brownies", "Juices", "Coffee", "Tea"] # List of items in the cafe.

stock = {"Cupcakes": 500,                                                           # Stock shows user how many of each item there are in dictionary format.
         "Muffins": 450,                                                            
         "Sandwiches": 550,
         "Brownies": 310,
         "Juices": 300,
         "Coffee": 400,
         "Tea": 430}

prices = {"Cupcakes": 2.25,                                                         # Prices shows user how much each item costs in dictionary format.
          "Muffins": 1.85,
          "Sandwiches": 3.99,
          "Brownies": 2.49,
          "Juices": 2.99,
          "Coffee": 2.25,
          "Tea": 2.20}

total_stock = 0

for item in menu:                                                                   # For each item in the menu, the stock and price are multiplied together.
    try:
        item_value = stock[item] * prices[item]
        total_stock += item_value
        print(f"The item value of {item} in stock: £{item_value:.2f}")              # Function prints out each value of each item using :.2f function.
    except KeyError as e:    
        print(f"Error: {e} not found in stock or prices dictionaries.")

print(f"The total stock worth of the cafe is: £{total_stock:.2f}")                  # Total stock is shown to user with all numbers added together.
