#Q10. Keep asking the user for input until they type "exit"

while True:

    something = input("Write something: ")

    if something == "exit":
        break

    print(f"You write: {something}")