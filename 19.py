#Check if a year entered by the user is a leap year or not.

year = int(input("Enter a year: "))

if(year % 4 == 0 and (year % 100 != 0) or ((year % 100 == 0) and (year % 400 == 0 ))):
    print("Leap year")

else:
    print("Not leap year")
