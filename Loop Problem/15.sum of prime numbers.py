#Sum of prime numbers

number = int(input("Enter a number: ")) # 5 that means (2-5) 2,3
vag_geche = False
sum = 0

for item in range(2, number):
    for items in range(2, number):
        if number % item == 0 :
            vag_geche = True
            break

if vag_geche:
    print("not prime")

else:
    print("prime")
    sum = sum + number
    print(sum)

