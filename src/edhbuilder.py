from .createDeck import create_deck
from .viewDecks import view_decks

def edhbuilder():
    print("++++++++++++++++++++++")
    print("Welcome to EDH Builder")
    print("++++++++++++++++++++++")
    while (True):
        print("\n=============================")
        print("1. Start building a new deck\n2. Edit an existing deck\n3. View all decks")
        print("=============================")
        menu_selection = input("Enter a selection (q to quit): ")
        match menu_selection:        
            case "q":
                break
            case "1":
                create_deck()
            case "3":
                view_decks()
            case _:
                print("Invalid selection")
    print("Goodbye!")
