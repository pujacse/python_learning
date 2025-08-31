# Inheritance:

# parent class,super class,base class

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"My name is : {self.fname} {self.lname}")

# child class,sub_class,derived class

class Student(Person):
    pass

p1 = Student("Puja","Das")
p1.printname()
