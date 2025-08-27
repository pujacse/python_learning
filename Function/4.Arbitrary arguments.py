# Arbitrary arguments:

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("tonu","monu","puja")


# another:
def my_function(child3,child2,child1):
    print("The youngest child is " + child3)

my_function(child1="tonu",child2="monu",child3="puja")