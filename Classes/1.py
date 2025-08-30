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
    "gadget": "ipad",

    "account":"1334",
    "balance" : 211321.86,
    'password':"1312"

}
print(thisdict4.values())

age = 10
name = "something"
ll = [1,2,3]



class Person:
    def __init__(self, name, age, cgpa, gadgets, balance):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.gadgets = gadgets
        self.balance = balance

    def withdrawal_money(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("Done!!!")
        else:
            print("I don't have enough balance!")

    def __str__(self):
        return f"{self.name} : {self.gadgets} -- {self.balance}"

puja = Person("Puja", 23, 3.60, ["iPhone", "Mac"], 10000)
# print(puja.name, puja.age, puja.cgpa, puja.gadgets)
# print(f"Balance: {puja.balance}")
# puja.withdrawal_money(500)
# print(f"Balance: {puja.balance}")
# puja.withdrawal_money(9999)
print(puja)


sm = Person("S", 29, 3.89, ["samsung", "Mac"], 0)
# print(sm.name, sm.age, sm.cgpa, sm.gadgets)
print(sm)

