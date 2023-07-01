product1 = input("Enter the first product name: ")
product2 = input("Enter the second product name: ")
product3 = input("Enter the third product name: ")

price1 = float(input("Enter the first product price: "))
price1 = round(price1, 2)
price2 = float(input("Enter the second product price: "))
price2 = round(price2, 2)
price3 = float(input("Enter the third product price: "))
price3 = round(price3, 2)

total_price = sum([price1, price2, price3])
average_price = total_price / len([price1, price2, price3])
print(f"The Total of {product1}, {product2}, {product3} is {total_price} and the average price of the items is {average_price}")

"""
It's probably better to input data into a dictionary, as I can recall keys and values.

shopping = {}

for i in range(3):
    product = input("Enter product name: ")
    price = float(input("Enter product's price: "))
    shopping[product] = price


# Total price of products in shopping
print(sum(shopping.values()))

# Average price of products in shopping
print(sum(shopping.values())/len(shopping))
"""



