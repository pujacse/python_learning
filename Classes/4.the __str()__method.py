# The __str__() method:

class Person:
    def __init__(self,names,age):
        self.name = names
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Puja", 23)
print(p1)