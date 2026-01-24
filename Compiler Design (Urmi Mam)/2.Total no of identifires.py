# program to list total number of identifiers from a c/c++ code snippet.

import re

keywords = {"int"}

code = """int a,b,sum
sum = a+b"""

tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)

identifiers = [word for word in tokens if word not in keywords]

print("Identifiers found:", identifiers)
print("Total identifiers:", len(identifiers))
print("Unique identifiers:", set(identifiers))