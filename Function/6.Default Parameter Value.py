# Default Parameter Value:

def my_function(country="norway"):
    print("I am from " + country)

my_function("sweden")
my_function("mali")
my_function()
my_function("Brazil")


# Passing a List as an Argument

fruits = ["apple","banana","mango"]
for item in fruits:
    print(item)

number = [1,2,3]
for items in number:
    print(items)

names = ["puja","sudarshan","moni"]
for name in names:
    print(name)

def my_function(items):
    # print("printing the items: ")
    for item in items:
        print(item)
    # print("all items are printed")

fruits = ["apple","banana","mango"]
my_function(fruits)

numbers = [1,2,3]
my_function(numbers)

names = ["puja","sudarshaan","moni"]
my_function(names)