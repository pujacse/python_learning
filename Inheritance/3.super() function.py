# Add property:

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"My name is : {self.fname} {self.lname}")

class Student(Person):
    def __init__(self,fname,lname,year):

        # To keep the inheritance of the parent's __init__() function,
        # add a call to the parent's __init__() function:

        Person.__init__(self,fname,lname)
        # OR
        super().__init__(fname,lname)

        # Add property:
        self.graduationyear = year

p1 = Student("Puja","Das", 2021)
print(p1.graduationyear)