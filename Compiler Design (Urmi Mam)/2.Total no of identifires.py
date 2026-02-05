# program to list total number of identifiers from a c/c++ code snippet.

import re # regular expression

keywords = {"int","float"}

code = """float a,b,sum
sum = a+b"""

tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
# r' means raw string
# \b means boundary

identifiers = [word for word in tokens if word not in keywords]

print("Identifiers found:", identifiers)
print("Total identifiers:", len(identifiers))
print("Unique identifiers:", set(identifiers))
# set() --- duplicate removal