# if dictionary

car = {
    "brand" : "Ford",
    "color" : "red",
    "year" : 1964
}
if "brand" in car:
    print("yes, 'model' is one of the keys in the thisdict dictionary")


# update dictionary

car = {
    "brand" : "Ford",
    "color" : "red",
    "year" : 1964
}
car.update({"brand" : "hybride"})
print(car.values())