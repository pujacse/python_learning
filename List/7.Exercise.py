#Exercise problem:
#Write a program to remove the duplicates in a list.


numbers = [2, 4, 1, 5, 4, 5]

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)