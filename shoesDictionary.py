shoes = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

shoes["Jordan 13"] += 4
shoes["Yeezy"] += 5
shoes["Foamposite"] += 4
shoes["Air Max"] += 4
shoes["SB Dunk"] += 2 

Jordan13 = shoes["Jordan 13"]
Jordan132 = shoes["Jordan 13"]
Yeezy = shoes["Yeezy"]
Yeezy2 = shoes["Yeezy"]
Foamposite = shoes["Foamposite"]
Foamposite2 = shoes["Foamposite"]
AirMax = shoes ["Air Max"]
SBDunk = shoes["SB Dunk"]

print(Jordan13)
print(Yeezy)
print (Foamposite)
print(AirMax)
print(SBDunk)

def restock(shoes, x):
    shoeValue = shoes * x
    return shoeValue

def clearanceSale(shoes, x):
    shoeSale = shoes / x
    return shoeSale


print(restock(Jordan13, 3))
print(clearanceSale(Foamposite, 2))
  
















