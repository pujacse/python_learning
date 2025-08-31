# the __init__() method:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Puja",36)

print(p1)

print(f"name : {p1.name}")
print(f"age : {p1.age}")