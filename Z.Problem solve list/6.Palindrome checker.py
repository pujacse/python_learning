# Palindrome checker - Check a given string reads the same backward and forward

string = input("Enter a string: ")

revers = string[::-1]

if string == revers:
    print("String is palindrome.")

else:
    print("String is not palindrome.")