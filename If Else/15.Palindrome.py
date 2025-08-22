#Palindrome Checks


word = input("Enter a word: ")

revers = word[::-1]

if word == revers:
    print("Word is Palindrome")

else:
    print("Word is not Palindrome")