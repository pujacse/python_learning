# Classes in Python:

"""
name - puja (4 people)
age - 23
cgpa - 3.60
gadget - iphone,macbook,ipad,Pc
"""
names =["puja","mitu","toyeba","moni"]

thisdict1 = {
    "name" : "puja",
    "age" : 23,
    "cgpa" : 3.60,
    "gadget": ["iphone","mobile","laptop"]
}
print(thisdict1.values())

thisdict2 = {
    "name" : "mitu",
    "age" : 22,
    "cgpa" : 3.61,
    "gadget": "mobile"
}
print(thisdict2.values())

thisdict3 = {
    "name" : "toyeba",
    "age" : 20,
    "cgpa" : 3.00,
    "gadget": "mobile"
}
print(thisdict3.values())

thisdict4 = {
    "name" : "moni",
    "age" : 19,
    "cgpa" : 2.61,
    "gadget": "ipad"
}
print(thisdict4.values())


class Person:
    def __init__(self, name, age, cgpa, gadgets):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.gadgets = gadgets



puja = Person("Puja", 23, 3.60, ["iPhone", "Mac"])
print(puja.name, puja.age, puja.cgpa, puja.gadgets)

