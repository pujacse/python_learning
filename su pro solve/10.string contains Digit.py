#Question 10: String Contains Digit.
#Write a Python program that takes a string as input.
#Determine if the string contains at least one digit (0-9).
#Print "Contains digit" or "Does not contain digit".

string = input("Enter a string: ")

if "0" in string or "1" in string or "2" in string or "3" in string or "4" in string or "5" in string or "6" in string or "7" in string or "8" in string or "9" in string :
    print("contains digit")

else:
    print("does not contain digit")