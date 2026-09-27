import json

def ajouter(Livre):
  
    id=int(input("donner le l id : "))
    titre=input("Donner le Titre : ")
    auteur=input("Donner l auteur : ")
    disponible=True
    Livre.append({'id':id,'titre':titre,'auteur':auteur,'disponible':disponible})
    sauvegarder(Livre,"Livre.json") 
    
  
    


def afficher(Livre):
  for livre in Livre :
    print("Titre : ", livre['titre'])
    print("auteur : ", livre['auteur'])
    print("disponible : ", livre['disponible'])

def rechercher(Livre, id ):
  trouver=False
  for livre in Livre :
    if livre['id']==id:
      print("Titre : ", livre['titre'])
      print("auteur : ", livre['auteur'])
      print("disponible : ", livre['disponible'])
      trouver=True
      break
  if trouver==False:
    print("pas trouver")
    

def Emprunter(Livre , titre):
  trouver=False
  for livre in Livre :
    if livre['titre']==titre:
      print("Titre : ", livre['titre'])
      print("auteur : ", livre['auteur'])
      print("disponible : ", livre['disponible'])
      if livre['disponible']==True:
        livre['disponible']=False
      else:
        print("Desoler ce livre n est pas disponible")
      trouver=True
      sauvegarder(Livre,"Livre.json") 

      break
  if trouver==False:
    print("pas trouver")


def rendre(Livre , id):
  trouver=False
  for livre in Livre :
    if livre['id']==id:
      print("Titre : ", livre['titre'])
      print("auteur : ", livre['auteur'])
      print("disponible : ", livre['disponible'])
      if livre['disponible']==False:
        livre['disponible']=True
      else:
        print("Desoler ce livre n a pas ete emprunter disponible")
      trouver=True
      sauvegarder(Livre,"Livre.json") 

      break
  if trouver==False:
    print("pas trouver")


def supprimer(Livre , id):
    
  for livre in Livre :
    if livre['id']==id:
      print("Titre : ", livre['titre'])
      print("auteur : ", livre['auteur'])
      print("disponible : ", livre['disponible'])
      Livre.remove(livre)
      sauvegarder(Livre,"Livre.json") 

      break


def sauvegarder(Livre, fichier):
  with open(fichier,'w') as f:
    json.dump(Livre,f,ensure_ascii=False,indent=4)

def charger(fichier):
  try:
    with open(fichier,'r') as f:
      return json.load(f)
  except FileNotFoundError:
    return []
  

def main():
  
  Livres= charger("Livre.json")

  ajouter(Livres)
  ajouter(Livres)
  ajouter(Livres)
  ajouter(Livres)
  ajouter(Livres)
  ajouter(Livres)
  ajouter(Livres)
  ajouter(Livres)
  ajouter(Livres)

  afficher(Livres)

  rechercher(Livres, 3)

  Emprunter(Livres,'les os')

  rendre(Livres,4)

  supprimer(Livres,4)

  sauvegarder(Livres,"Livre.json") 
  
if __name__ == "__main__":
 main()
