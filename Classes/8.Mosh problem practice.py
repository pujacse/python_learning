# Mosh practice:

class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print("My name is : " + self.name)
        # OR
        print(f"My name is : {self.name}")

p1 = Person("puja")
p1.talk()