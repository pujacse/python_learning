# Add methods / function:

# print - Welcome Mike Olsen to the class of 2024

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"My name is : {self.fname} {self.lname}")

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        # Add property:
        self.graduationyear = year

    def Function(self):
        print (f"Welcome {self.fname} {self.lname} to the class of {self.graduationyear}")

p1 = Student("Mike","Olsen", 2024)
p1.Function()