#Sum of prime numbers

number = int(input("Enter a number: ")) # 5 that means (2-5) 2,3
vag_geche = False
sum = 0

for item in range(1, number + 1):
    vag_geche = False

    for i in range(2, item):
        if item % i == 0 :
            vag_geche = True
            print("not prime")
            break

    if vag_geche == False:
        sum = sum + item

print(f"sum of prime numbers: {sum}")



