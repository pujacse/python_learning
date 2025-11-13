# Read three floats from input and
# print their average with 2 decimal places.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
avg = (a + b + c)/3
print(f"Their average: {avg: .2f}")