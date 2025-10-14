from .builderMode import builder_mode
from .utils.deckHelper import create_deck_file

def create_deck():
    deck_name = ""
    while deck_name == "":
        deck_name = input("Please enter a name for the deck (q to quit back to menu): ")
        if deck_name == "q":
            return
        elif deck_name == "":
            print("Deck name cannot be blank")
    deck_commander = ""
    while deck_commander == "":
        deck_commander = input("Please enter the commander (q to quit back to menu): ")
        if deck_commander == "q":
            return
        elif deck_commander == "":
            print("Deck must have a commander")
    create_deck_file(deck_name)
    builder_mode(deck_name, deck_commander)