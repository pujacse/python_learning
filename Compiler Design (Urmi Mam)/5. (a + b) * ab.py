# (a + b) * ab :

import re

pattern = r'^(a|b)*ab$'

string = input("Enter a string: ")

# Check if string matches the pattern
if re.match(pattern, string):
    print("Valid String")

else:
    print("Invalid String")

