#Question 8: Range Check with and.
#Write a Python program that asks the user to enter an integer.
#Check if the number is between 1 and 100 (inclusive).
#If it is, print "Number is in range".
#Otherwise, print "Number is out of range".

number = int(input("Enter a number: "))

if 1 <= number <= 100:
    print("number is in range.")

else:
    print("number is out of range.")