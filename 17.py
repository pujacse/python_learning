#Write a program that prints "Good Morning" if the current time is before 12 PM, else print "Good Afternoon".

time = int(input("Enter current time: "))
from datetime import datetime
current_hour = datetime.now().hour

if time >= 12 :
    print("Good Afternoon")

else:
    print("Good Morning.")