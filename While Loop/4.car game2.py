# car game:
# >help: start - to start the car
#        stop - to stop the car
#        quit - to exit
# >asd : I don't understand that
# >start : car started..Ready to go!
# >stop : car stopped

command = "" # car
started = False # engine

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started...")

    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
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