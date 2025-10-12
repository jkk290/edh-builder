import os

def get_decks():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    decks_path = os.path.abspath(os.path.join(current_dir, "../..", "decks"))
    os.makedirs(decks_path, exist_ok=True)

    current_decks = os.listdir(decks_path)
    if len(current_decks) == 0:
        print("No decks found")
        return
    deck_list = []
    for deck in current_decks:
        deck_name, deck_ext = os.path.splitext(deck)
        if deck_ext.lower() == ".csv":
            deck_list.append(deck_name)
    return deck_list