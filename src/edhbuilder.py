def edhbuilder():
    print("Welcome to EDH Builder")
    print("=============================")
    print("1. Start building a new deck\n2. Edit an existing deck\nq to exit")
    print("=============================")
    while (True):
        
        user_input = input("Enter a selection: ")
        if (user_input == "q"):
            break
        elif (user_input == "1"):
            print("")
        elif (user_input != '1' and user_input != '2'):
            print("Invalid selection")
    print("goodbye")
