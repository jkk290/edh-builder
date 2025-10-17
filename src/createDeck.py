from .builderMode import builder_mode
from .utils.deckHelper import create_deck_file, write_deck_file

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
    background_or_partner = True
    deck_background = None
    deck_partner = None
    while background_or_partner:
        print("Will your deck have a background or partner?\n1. Background\n2. Partner\n3. None")
        response = input("Please enter 1-3 (q to quit back to menu): ")
        match response:
            case "1":
                deck_background = input("Enter the background card name: ")
                break
            case "2":
                deck_partner = input("Enter the partner card name: ")
                break
            case "3":
                background_or_partner = False
            case _:
                print("Invalid selection")
    deck_companion = input("Enter card name if deck has a companion. Otherwise, enter \"n\" or leave blank (q to quit back to menu): ")
    if deck_companion == "q":
        return

    deck_content = [{"card_name": deck_commander, "type": "commander", "qty": 1}]
    if deck_companion != "n" and deck_companion != "":
        deck_content.append({"card_name": deck_companion, "type": "companion", "qty": 1})
    if background_or_partner and deck_background:
        deck_content.append({"card_name": deck_background, "type": "background", "qty": 1})
    elif background_or_partner and deck_partner:
        deck_content.append({"card_name": deck_partner, "type": "partner", "qty": 1})
    create_deck_file(deck_name)
    write_deck_file(deck_name, deck_content)
    builder_mode(deck_name)