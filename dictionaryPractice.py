groceries = {"chicken": 1.59, "beef": 1.99, "cheese": 1.00, "milk": 2.5}

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

def totalPrice(price1, price2):
    addPrice = price1 + price2
    return addPrice

def differenceInPrice(price1, price2):
    subtractPrice = price1 - price2
    if subtractPrice < 0:
        return -subtractPrice
    else: 
        return subtractPrice 

print(totalPrice(chicken_price, beef_price))
print(differenceInPrice(chicken_price, beef_price))
print(differenceInPrice(beef_price, cheese_price))
