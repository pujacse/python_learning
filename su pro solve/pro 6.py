#Question 6: Substring Check.
#Write a Python program that asks the user
#for two strings: a main string and a substring.
#Print "Substring found" if the substring is present in the main string,
#otherwise print "Substring not found"

string = input("Enter a main string: ")
substring = input("Enter a substring: ")

if substring in string:
    print("Substring found")

else:
    print("Substring not found")