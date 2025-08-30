# Classes in Python:

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

