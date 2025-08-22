#Question 7: Palindrome Check (Simplified)
#Write a Python program that takes a word as input.
#Determine if the word reads the same forwards and backward (a palindrome). Ignore case for this problem. Print "It's a palindrome!" or "Not a palindrome.".

word = input("Enter a word: ")

reverse = word[::-1]
print(f"reverse : {reverse}")

if word == reverse:
    print("Its palindrome.")
else:
    print("Its not palindrome.")