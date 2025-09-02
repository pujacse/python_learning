# Multiplication table - print the multiplication table of a number(e.g.,5).

number = int(input("Enter a number: "))

for item in range(1, 11):
    print(f" {number} * {item} = {number * item}")