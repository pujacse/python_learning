#Ask the user for a number. If the number is divisible by 3,
#print "Fizz", if divisible by 5, print "Buzz", if divisible by both, print "FizzBuzz".

number = int(input("Enter a number: "))

if number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")

else:
    print("FizzBuzz")