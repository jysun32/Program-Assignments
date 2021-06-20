cityList = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cityList)
print(cityList[0])
print(cityList[1])
print(cityList[2])

colorList = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "lilac", "lavender", "fuschia"]
print(colorList)
print(colorList[2])
print(colorList[7])
print(colorList[8])

fourCities = cityList[0:4]
fourColors = colorList[0:4]

print(fourCities)
print(fourColors)

cityList[0] = "San Francisco"
cityList[2] = "Brooklyn"
cityList[7] = "Hollywood"
cityList[5] = "Tampa"
print(cityList)

cityList.append("Oakland")
cityList.extend(["New York City", "Los Angeles"])
cityList.insert(0, "Miami")
print(cityList)

cityList.pop(1)
print(cityList)

cityList.remove("New York City")
print(cityList)

cityList.remove("Miami")
print(cityList)






