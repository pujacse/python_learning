# This program that asks our phone number. let's type 1234. we type it in digits and
# then this will translate it, to words,take a look. Enter, it prints, 1, 2, 3, 4

number = input("Enter phone number: ") #123

phone_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
for item in number: #123
    print(phone_number.get(item), end=" ")

# name = input("Enter your name: ")
# for item in name:
#     print(item)