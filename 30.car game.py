# car game:
# >help: start - to start the car
#        stop - to stop the car
#        quit - to exit
# >asd : I don't understand that
# >start : car started..Ready to go!
# >stop : car stopped

command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("car started..Ready to go!")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that")