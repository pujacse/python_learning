#write a program to find the largest number in a list.

numbers = [3,5,10,7,9]
max = numbers[0]
for item in numbers:
    if item > max:
        max = item
print(f"maximum number is: {max}")