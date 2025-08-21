#continue statement using while loop

i = 0

while i < 6:
    i = i + 1

    if i == 3:
        continue

    print(i)



#continue statement using for loop

numbers = [1,2,3,4,5,6]

for item in numbers:

    if item == 3:
        continue

    print(item)