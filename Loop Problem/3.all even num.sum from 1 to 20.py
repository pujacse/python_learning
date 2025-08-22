#Q3. Print all even numbers sum from 1 to 20

sum = 0
for item in range(1, 21):
    if item % 2 == 0:
        sum = sum + item
print(sum)


