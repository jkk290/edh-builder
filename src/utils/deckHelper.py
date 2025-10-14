import os

def get_decks_dir():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    decks_path = os.path.abspath(os.path.join(current_dir, "../..", "decks"))
    os.makedirs(decks_path, exist_ok=True)
    return decks_path

def get_decks():
    decks_path = get_decks_dir()

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

def create_deck_file(deck_name):
    decks_path = get_decks_dir()

    file_name = f"{deck_name}.csv"
    full_path = os.path.join(decks_path, file_name)
    with open(full_path, "w") as f:
        pass
    print(f"{deck_name}.csv successfully created")