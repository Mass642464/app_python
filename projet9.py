class Livre :
    def __init__(self,id , Titre, auteur , disponible):
        self.id=id
        self.titre=Titre
        self.auteur=auteur
        self.disponible=disponible
    
    def afficher_livre(self):
        print("Id :", self.id)
        print("Titre : ", self.titre)
        print("Auteur : ", self.auteur)
        print("Disponible : ", self.disponible)

    def emprunter(self ):
        if self.disponible==True:
            self.disponible=False
            print("livre : ",self.id,"a ete Emprunter")
        else:
            print("Livre indisponible ")
    
    def retourner(self):
        if self.disponible==False:
            self.disponible=True
            print("livre : ",self.id,"a ete Retouner")
        else:
            print("Livre N a pas ete emprunter ")
    
class Utilisateur :
    def __init__(self, id , nom ):
       self.id =id
       self.nom=nom
       self.livre_emprunter=[]
    
    def afficher(self):
        print("id Utilisateur : " , self.id)
        print("Nom Utilisateur : ", self.nom)
        for livre in self.livre_emprunter:
            livre.afficher_livre()
    
    def emprunter(self, liste):
        titre = input("donner le titre du livre a emprunter : ")
        trouver = False
        for livre in liste:
            if livre.titre == titre:
                trouver = True
                if livre.disponible:
                    self.livre_emprunter.append(livre)
                    livre.emprunter(titre)
                else:
                    print("Livre indisponible")
                break
        if trouver == False:
            print("ce livre ne se trouve pas dans notre liste de livre")

    def rendre_livre(self, id):
        for livre in self.livre_emprunter:
            if livre.id == id:
                livre.retourner(id)
                self.livre_emprunter.remove(livre)
                return
        print("Aucun livre emprunté avec cet id")

class Bibliotheque:
    def __init__(self, nom ):
        self.nom = nom 
        self.livre=[]
        self.utilisateur=[]

    def ajouter_livre(self , livre):
        self.livre.append(livre)

    def ajouter_utilisateur(self , utilisateur):
        self.utilisateur.append(utilisateur)
    
    def afficher_livre(self):
        for livre in self.livre:
            livre.afficher_livre()
    
    def afficher_utilisateur(self):
        for utili in self.utilisateur:
            utili.afficher()
    
    def rechercher_livre(self, id):

      for livre in self.livre:
        if livre.id == id:
            return livre

      return None
    
    def rechercher_utilisateur(self, id):
        for utilisateur in self.utilisateur:
            if utilisateur.id==id:
                return utilisateur
        return None
    

def menu() -> str:
    print("\n--- Menu Bibliothèque ---")
    print("1. Afficher les livres")
    print("2. Afficher les utilisateurs")
    print("3. Emprunter un livre")
    print("4. Rendre un livre")
    print("0. Quitter")
    return input("Choix: ").strip()


def main():
    bibliotheque = Bibliotheque("Bibliothèque Centrale")

    bibliotheque.ajouter_livre(Livre(1, "Le Petit Prince", "Antoine de Saint-Exupéry", True))
    bibliotheque.ajouter_livre(Livre(2, "1984", "George Orwell", True))
    bibliotheque.ajouter_livre(Livre(3, "L'Alchimiste", "Paulo Coelho", True))

    utilisateur = Utilisateur(1, "Alice")
    bibliotheque.ajouter_utilisateur(utilisateur)

    while True:
        choix = menu()

        if choix == "1":
            bibliotheque.afficher_livre()
        elif choix == "2":
            bibliotheque.afficher_utilisateur()
        elif choix == "3":
            utilisateur.emprunter(bibliotheque.livre)
        elif choix == "4":
            try:
                id_livre = int(input("Entrez l'id du livre à rendre: "))
            except ValueError:
                print("Id invalide")
            else:
                utilisateur.rendre_livre(id_livre)
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()


               