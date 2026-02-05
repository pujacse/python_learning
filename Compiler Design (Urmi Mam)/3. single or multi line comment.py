# Program to check if a comment is single-line comment or multi-line comment.

comment = input("Enter a comment: ")

if comment.startswith("//"):
    print("Single-line comment")

elif comment.startswith("/*") and comment.endswith("*/"):
    print("Multi-line comment")

else:
    print("Not a valid comment")
