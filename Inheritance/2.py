# To keep the inheritance of the parent's __init__() function,
# add a call to the parent's __init__() function:

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"My name is : {self.fname} {self.lname}")

class Student(Person):
    def __init__(self,fname,lname):

        # To keep the inheritance of the parent's __init__() function,
        # add a call to the parent's __init__() function:
        Person.__init__(self,fname,lname)

p1 = Student("Puja","Das")
p1.printname()