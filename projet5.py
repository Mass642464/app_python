
import json

def charger():
    try:
        with open("University.json", "r", encoding="utf-8") as university_file:
            contenu = university_file.read().strip()
            if not contenu:
                return {}
            return json.loads(contenu)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    except Exception as error:
        print(f"Erreur lors du chargement de University.json : {error}")
        return None


def Sauvegarder(donnees):
    try:
        with open("University.json", "w", encoding="utf-8") as university_file:
            json.dump(donnees, university_file, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print(f"Erreur lors de la sauvegarde dans University.json : {error}")
        return False

def creer_University():
    try :
        NOM = input("donner le nom de l'université : ")
        ufrs = []
        recteur = input("Donner le nom du recteur : ")
        return {'nom': NOM, 'ufrs': ufrs, 'recteur': recteur}
    except ValueError as error:
        print("la Creation a echoue ")

def creer_Ufr():
    """Crée un dictionnaire UFR avec listes vides (clés en minuscules, pluriel)."""
    nom = input("Donner le nom de l'ufr : ")
    directeur = input("Donner le nom du directeur : ")
    professeurs = []
    etudiants = []
    administrateurs = []
    return {'nom': nom, 'directeur': directeur, 'professeurs': professeurs, 'etudiants': etudiants, 'administrateurs': administrateurs}

def Ajouter_proffesseur(ufr):
    """Demande les infos d'un professeur et renvoie un dict (clés minuscules).
    """
    matricule = input("Donner le matricule du professeur : ")
    nom = input("Donner le nom du professeur : ")
    matiere = input("Donner la matière qu'il enseigne : ")
    return {'matricule': matricule, 'nom': nom, 'matiere': matiere, 'ufr': ufr}

def afficher_professeur(professeur):
    """Affiche les informations d'un professeur en évitant les KeyError."""
    print("matricule :", professeur.get('matricule', 'N/A'))
    print("nom :", professeur.get('nom', 'N/A'))
    print("matiere :", professeur.get('matiere', 'N/A'))

def rechercher(university ,matricule):
    if not university:
        print("Données university vides.")
        return None
    ufrs = university.get('ufrs') or university.get('UFR') or []
    trouver = False
    for ufr in ufrs:
        # étudiants
        for etudiant in ufr.get('etudiants', []) + ufr.get('Etudiant', []):
            if etudiant.get('matricule') == matricule:
                print("C'est un étudiant")
                afficher_etudiant(etudiant)
                trouver = True
                break
        if trouver:
            break
        # professeurs
        for professeur in ufr.get('professeurs', []) + ufr.get('Professeur', []) + ufr.get('professeur', []):
            if professeur.get('matricule') == matricule:
                print("C'est un professeur")
                afficher_professeur(professeur)
                trouver = True
                break
        if trouver:
            break
        # administrateurs
        for administrateur in ufr.get('administrateurs', []) + ufr.get('Administrateur', []) + ufr.get('administrateur', []):
            if administrateur.get('matricule') == matricule:
                print("C'est un administrateur")
                afficher_administrateur(administrateur)
                trouver = True
                break
        if trouver:
            break
    if not trouver:
        print("Cette personne ne se trouve pas dans l'université.")
                   
def Ajouter_Etudiant(ufr):
    """Demande les infos d'un étudiant et renvoie un dict (clés minuscules)."""
    matricule = input("Donner le matricule de l'etudiant : ")
    nom = input("Donner le nom de l'etudiant : ")
    niveau = input("Quel est votre niveau : ")
    return {'matricule': matricule, 'nom': nom, 'niveau': niveau, 'ufr': ufr}

def afficher_etudiant(etudiant):
    print("matricule :", etudiant.get('matricule', 'N/A'))
    print("nom :", etudiant.get('nom', 'N/A'))
    print("niveau :", etudiant.get('niveau', 'N/A'))

def Ajouter_Administrateur(ufr):
    """Demande les infos d'un administrateur et renvoie un dict (clés minuscules)."""
    matricule = input("Donner le matricule de l'administrateur : ")
    nom = input("Donner le nom de l'administrateur : ")
    return {'matricule': matricule, 'nom': nom, 'ufr': ufr}

def afficher_administrateur(administrateur):
    print("matricule :", administrateur.get('matricule', 'N/A'))
    print("nom :", administrateur.get('nom', 'N/A'))
    



def menu() -> str:
    print('\n--- Menu University ---')
    print('1. Créer une university')
    print('2. Créer une UFR')
    print('3. Ajouter un professeur')
    print('4. Ajouter un étudiant')
    print('5. Ajouter un administrateur')
    print('6. Lister les UFR')
    print('7. Rechercher par matricule')
    print('8. Charger depuis le fichier')
    print('9. Sauvegarder dans le fichier')
    print('0. Quitter')
    return input('Choix: ').strip()


def main():
   print("===============================")

if __name__ == '__main__':
    main()


