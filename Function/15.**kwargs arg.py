def my_keyword_arguments(**kwargs):
    for key , value in kwargs.items():
        print(key, value)

my_keyword_arguments(a = 1, b = 2, c = 3, d = 4)
my_keyword_arguments(x = 's',y = 'e')


# another example :

name = "variable outside function"
def my_function():
    return name

print(my_function())
print(name)


# another:
name = "variable outside function"
def my_function():
    name = "variable inside function"
    return name

print(my_function())
print(name)


# another example:
name = "variable outside function"
def my_function():
    global name
    name = "variable inside function"
    return name

print(my_function())
print(name)