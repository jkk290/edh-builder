import re
from .utils.deckHelper import get_deck_content

def print_deck_content(deck_content):
    print("Current deck list")
    print("+++++++++++++++++\n")
    for line in deck_content:
        print(f"{line} - {deck_content[line]}")
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
                return
            case "show deck":
                print_deck_content(deck_content)
            case s if s.startswith("add "):
                splitted_input = builder_input.split(" ", 1)
                has_qty = re.search("[-][0123456789]+$", splitted_input[1])
                if has_qty:
                    final_input = splitted_input[1].split(" -")
                    deck_content[final_input[0]] = int(final_input[1])
                else:
                    deck_content[splitted_input[1]] = 1
            case s if s.startswith("delete "):
                splitted_input = builder_input.split(" ", 1)
                has_qty = re.search("[-][0123456789]+$", splitted_input[1])
                if has_qty:
                    final_input = splitted_input[1].split(" -")
                    qty = int(final_input[1])
                    if deck_content[final_input[0]] - qty > 0:
                        deck_content[final_input[0]] -= qty
                    else:
                        del deck_content[final_input[0]]
                else:
                    del deck_content[splitted_input[1]]      