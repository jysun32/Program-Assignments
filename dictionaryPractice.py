groceries = {"chicken": "$1.59", "beef": "$1.99", "cheese": "$1.00", "milk": "$2.50"}

chicken_price = groceries["chicken"]
chicken2_price = groceries["chicken"]
beef_price = groceries["beef"]
beef2_price = groceries["beef"]
cheese_price = groceries["cheese"]
cheese2_price = groceries["cheese"]
milk_price = groceries["milk"]

print(chicken_price)
print(beef_price)
print(cheese_price)
print(milk_price)

del groceries["chicken"]
del groceries["beef"]

print(chicken_price)
print(beef_price)
print(cheese_price)
print(milk_price)
