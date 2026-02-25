# Containing 'ab' as a substring:

import re

user_input = input("Enter a string: ")

if re.search(r"ab", user_input):
    # r মানে raw string (escape character সমস্যা এড়াতে ব্যবহার হয়)।
    print("Valid (String contains 'ab')")

else:
    print("Invalid (String does not contain 'ab')")

