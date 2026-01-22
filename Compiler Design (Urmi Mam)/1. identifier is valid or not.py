# program to identify whether an identifier is valid or not.

import keyword

identifier = input("Enter an identifier: ")

if identifier.isidentifier() and not keyword.iskeyword(identifier):
    print("Valid identifier")

else:
    print("Invalid identifier")