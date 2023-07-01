# menu containing 4 elements
menu = ['latte', 'mocha', 'cappuccino', 'flat white']

# inventory held for each menu item 
stock = {
    'latte' : 10, 
    'mocha': 11, 
    'cappuccino': 12, 
    'flat white': 13
    }

# price of each menu item 
price = {
    'latte' : 1, 
    'mocha': 2, 
    'cappuccino': 3, 
    'flat white': 4
    }

# stock value for each menu item 
stock_value={}
for idx, item in enumerate(menu):
    stock_value[item] = stock[item]*price[item]

# Total stock value
print(f"Total stock value: {sum(stock_value.values())}")
