from .createDeck import create_deck
from .editDeck import edit_deck
from .utils.deckHelper import get_decks

def edhbuilder():
    print("++++++++++++++++++++++")
    print("Welcome to EDH Builder")
    print("++++++++++++++++++++++")
    while (True):
        print("\n=============================")
        print("1. Start building a new deck\n2. Edit an existing deck\n3. View all decks")
        print("=============================\n")
        menu_selection = input("Select from the menu 1-3 (q to quit): ")
        match menu_selection:        
            case "q":
                break
            case "1":
                create_deck()
            case "2":
                edit_deck()
            case "3":
                deck_list = get_decks()
                for deck in deck_list:
                    print(deck)
            case _:
                print("Invalid selection")
    print("Goodbye!")