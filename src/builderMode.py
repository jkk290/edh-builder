def builder_mode(deck_name, deck_commander):
    print("==================")
    print("=  Builder Mode  =")
    print("==================")
    while True:
        builder_input = input("(builder)> ")
        if builder_input == "q":
            return
        