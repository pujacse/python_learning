#Q12. Count vowels in a string

string = input("Enter a string: ")
vowels = "aeiouAEIOU"

count = 0

for item in string:
    if item in vowels:
        count = count + 1

print(f"count: {count}")
