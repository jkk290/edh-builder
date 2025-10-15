from .utils.deckHelper import get_decks, delete_deck_file
from .builderMode import builder_mode

def delete_deck():
    while True:
        deck_list = get_decks()
        print("\n=====================")
        for i in range(len(deck_list)):
            print(f"{i+1}. {deck_list[i]}")
        print("=====================\n")
        deck_selection = ""
        if len(deck_list) == 1:
            deck_selection = input(f"Select a deck, enter 1 (q to quit back to menu): ")
        else:
            deck_selection = input(f"Select a deck, enter 1-{len(deck_list)} (q to quit back to menu): ")
        if deck_selection == "q":
            return
        try:
            selection_converted = int(deck_selection)
            if selection_converted - 1 in range(len(deck_list)):
                deck_name = deck_list[int(deck_selection) - 1]
                print(f"Deleting {deck_name}")
                delete_deck_file(deck_name)
            else:
                raise Exception
        except Exception:
            print("Invalid selection")
        
