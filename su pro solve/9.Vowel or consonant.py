#Question 9: Vowel or Consonant.
#Write a Python program that takes a single letter (a-z or A-Z) as input.
#Using if-elif-else statements,
#determine if it's a vowel (a, e, i, o, u, case-insensitive) or a consonant. Print your finding. Assume valid single-letter input.

letter = input("Enter a letter: ")

if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or
    letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U"):
    print("letter is vowel")

elif "a" <= letter <= "z" or "A" <= letter <= "Z" :
    print("letter is consonant")
else:
    print("others")