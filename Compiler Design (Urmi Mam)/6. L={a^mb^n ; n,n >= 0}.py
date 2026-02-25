import re

pattern = r'^a*b*$'

string = input("Enter a string: ")

if re.match(pattern, string):
    print("Valid String")
else:
    print("Invalid String")

