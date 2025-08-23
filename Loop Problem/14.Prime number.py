# Prime Number Print

number = int(input("Enter a number: ")) # 6
vag_geche = False

for item in range(2, number): # 2, 3, 4 5
    if number % item == 0:
        vag_geche = True
        break

if vag_geche:
    print("not prime")
else:
    print("prime")
