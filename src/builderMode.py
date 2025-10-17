import re
from .utils.deckHelper import get_deck_content, write_deck_file
from .utils.manual import manual

def print_deck_content(deck_content):
    print("Current deck list")
    print("+++++++++++++++++\n")
    for card in deck_content:
        if card["type"] != "":
            print(f"{card["card_name"]} - {card["type"]} - x{card["qty"]}")
        else:
            print(f"{card["card_name"]} - x{card["qty"]}")
    print("====================\n")

def builder_mode(deck_name):
    print("==================")
    print("=  Builder Mode  =")
    print("==================\n")

    try:
        deck_content = get_deck_content(deck_name)
    except Exception:
        print("Error getting deck")

    print_deck_content(deck_content)

    while True:
        builder_input = input("(builder)> ")
        match builder_input:
            case "q":
                quit_input = ""
                while quit_input.lower() != "y" and quit_input.lower() != "n":                    
                    quit_input = input("Save current deck list to file? (y/n): ")
                    if quit_input != "y" and quit_input != "n":
                        print("Invalid response, please enter y or n")

                if quit_input.lower() == "y":
                    print(f"Saving deck to file {deck_name}.csv")
                    write_deck_file(deck_name, deck_content)
                return
            case "show deck":
                print_deck_content(deck_content)
            case s if s.startswith("add "):
                splitted_input = builder_input.split(" ", 1)
                has_qty = re.search("[-][0123456789]+$", splitted_input[1])
                if has_qty:
                    final_input = splitted_input[1].split(" -")
                    deck_content.append({"card_name": final_input[0], "type": "", "qty": int(final_input[1])})
                else:
                    deck_content.append({"card_name": splitted_input[1], "type": "", "qty": 1})
            case s if s.startswith("delete "):
                splitted_input = builder_input.split(" ", 1)
                has_qty = re.search("[-][0123456789]+$", splitted_input[1])
                if has_qty:
                    final_input = splitted_input[1].split(" -")
                    for card in deck_content:
                        if card["card_name"].lower() == final_input[0].lower():
                            card_qty = int(card["qty"])
                            card["qty"] = card_qty - int(final_input[1])
                            if card["qty"] <= 0:
                                deck_content.remove(card)
                            break
                    else:
                        print(f"{final_input[0]} not found in deck list")
                else:
                    for card in deck_content:
                        if card["card_name"].lower() == splitted_input[1].lower():
                            deck_content.remove(card)
                            break
                    else:
                        print(f"{splitted_input[1]} not found in deck list")
            case "save deck":
                print(f"Saving deck to file {deck_name}.csv")
                write_deck_file(deck_name, deck_content)
            case "man":
                print(manual())
            case _:
                print("Invalid syntax, enter \"man\" to view the manual ")