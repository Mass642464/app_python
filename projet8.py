class Etudiant:
    def __init__(self,matricule,nom,age , note):
        self.matricule=matricule
        self.nom=nom
        self.age=age
        self.note=note

    def ajouter_note(self,note):
        self.note.append(note)
    
    def afficher(self):
        print("matricule : ", self.matricule)
        print("nom : ", self.nom)
        print("age : ", self.age)
        print("note : ",self.note)

    def moyenne(self):

     if len(self.note) == 0:
        return 0

     somme = 0

     for note in self.note:
        somme += note

     return somme / len(self.note)



def main ():
    note=[12]
    Etudiant1=Etudiant(6424,"mass",25,note)

    Etudiant1.ajouter_note(19)

    Etudiant1.afficher()

    print(Etudiant1.moyenne())


if __name__ == "__main__":
 main()
         
