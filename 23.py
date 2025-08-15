num = int(input("Enter a number: "))

if num <= 1:
    print("not prime number")

elif num == 2:
    print("prime number")

elif num > 2 and num % 2 == 0:
    print("not a prime number")

else:
    print("prime number")