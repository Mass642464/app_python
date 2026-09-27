import json

def ajouter_note(Notes, note):
    Notes.append(note)

def Afficher_note(Notes):
    for note in Notes:
        print(note)

def sauvegarder(Notes, fichier='Notes.json'):
    with open(fichier, 'w') as f:
        json.dump(Notes, f, ensure_ascii=False, indent=4)

def charger(fichier):
    try:
        with open(fichier, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def main():

    Notes = charger('Notes.json')

    ajouter_note(Notes, 12)
    ajouter_note(Notes, 14)
    ajouter_note(Notes, 15)

    Afficher_note(Notes)

    sauvegarder(Notes, 'Notes.json')

if __name__ == "__main__":
    main()