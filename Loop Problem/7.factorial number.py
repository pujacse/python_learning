#Q7. Find factorial of a number (say 5)


number = int(input("Enter a number: "))

fact = 1

for item in range(1, number+1):
    fact = fact * item

print(fact)