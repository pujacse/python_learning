# create methods:
# You can create your own methods inside objects:

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("puja", 23)
p1.myfunc()