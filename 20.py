#Check if a year entered by the user is a leap year or not.
year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("leap year")

else:
    print("Not leap year")
    print("Not leap year")