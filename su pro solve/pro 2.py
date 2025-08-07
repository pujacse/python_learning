#Question 2: String Concatenation.
#Write a Python program that asks the user
#for their first name and last name separately.
#Then,print their full name by joining the two strings
#with a space in between.

First = input ("Enter your first name: ")
Last = input ("Enter your last name: ")

Name = First + " " + Last

print(f"Full name: {Name}")