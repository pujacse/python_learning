# if dictionary

car = {
    "brand" : "Ford",
    "color" : "red",
    "year" : 1964
}
if "brand" in car:
    print("yes, 'model' is one of the keys in the thisdict dictionary")


# update dictionary or add

car = {
    "brand" : "Ford",
    "color" : "red",
    "year" : 1964
}
car.update({"brand" : "hybride"})
print(car.values())

# remove dictionary

car = {
    "brand" : "Ford",
    "color" : "red",
    "year" : 1964
}
car.pop("brand") # The pop() method removes the item with the specified key name.
car.popitem() # the "popitem()" removes the last inserted item.
print(car)

# The del keyword removes the item with the specified key name.

car = {
    "brand" : "Ford",
    "color" : "red",
    "year" : 1964
}
del car["brand"]
print(car)

# clear dictionary

car.clear()
print(car)
