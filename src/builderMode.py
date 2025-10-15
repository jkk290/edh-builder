from .utils.deckHelper import get_deck_content

def builder_mode(deck_name):
    print("==================")
    print("=  Builder Mode  =")
    print("==================")

    try:
        deck_content = get_deck_content(deck_name)
        print("+++++++++++++++++")
        print("Current deck list")
        print("+++++++++++++++++\n")
        for line in deck_content:
            print(f"{line} - {deck_content[line]}")
        print("====================\n")
    except Exception:
        print("error getting deck")

    while True:
        builder_input = input("(builder)> ")
        if builder_input == "q":
            return
        