# factorial function - Define a function that computes the factorial of a number.

number = int(input("Enter a number: "))

fact = 1

for item in range(1, number+1):
    fact = fact * item

print(f"factorial is: {fact}")