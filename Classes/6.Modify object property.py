# Modify object properties:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, My name is: " + self.name)

p1 = Person("Puja",25)
p1.age = 23
print(p1.age)


# Delete object property:
# del p1.age
# print(p1.age)
