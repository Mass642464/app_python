def Ajouter_bus(Bus):
    
    numero=input("Donner Le Numero du Bus (ex:B12) : ") 
    destination=input("Donner La Destitanion (ex: Dakar)")
    places= int(input("Donner Le Nombre de palce du Bus :"))
    passagers=[]
    Bus.append({'numero':numero, 'Destination':destination , 'Places':places, 'passagers':passagers})

def Ajouter_passager(Bus):
    while True:
            rep=input("Voulez vous Ajouter un passagers (oui/non) : ")
            if rep not in ["oui", "non"]:
               print("Valeur saisie incorrete vous devez ecrire oui ou non")
            elif rep=="oui":
                 passager=input("Donner le nom du Passager: ")
                 destination=input("Donner la destination : ")
                 dispo=False
                 for bus in Bus :
                      if bus['Destination']==destination:
                           if bus['Places']>len(bus['passagers']):
                                bus['passagers'].append(passager)
                                dispo=True
                                break 
                 if dispo==False:
                      print("Desoler Mais aucun bus n est diponible pour ce passager a ces destination")
            else:
                    break

def Afficher_Bus(Bus):
     if len(Bus)==0:
          print("Pas de Bus ")
     else:
          for bus in Bus:
               print("numero :", bus['numero'])
               print("Destination :", bus['Destination'])
               print("Places : ", bus['Places'])
               print("Le nombre des passagers : ", len(bus['passagers']))
    
def Rechercher_Bus(Bus):
     if len(Bus)==0:
          print("pas de Bus")
     else:
          b=input("les numero de bus a rechercher ")
          trouver= False
          for bus in Bus:
               if bus['numero']==b:
                    trouver=True
                    print("numero :", bus['numero'])
                    print("Destination :", bus['Destination'])
                    print("Places : ", bus['Places'])
                    print("Le nombre des passagers : ", len(bus['passagers']))
                    break
          if trouver==False:
               print("pas trouver")

def Afficher_passager_Bus(Bus):

     if len(Bus)==0:
          print("pas de bus")
     else:
          b=input("Donner le bus dont vous voulez afficher les passager : ")
          
          for bus in Bus:
               if bus['numero']==b:
                    for passager in bus['passagers']:
                     print(passager)
                    break

def supprimer_passager(Bus):
     if len(Bus)==0:
          print("pas de bus")
     else:
          b=input("Donner le bus dont vous voulez supprimer un passager : ")
          p=input("Donner le nom du passager a supprimer : ")
          for bus in Bus:
               if bus['numero']==b:
                    if p in bus['passagers']:
                         bus['passagers'].remove(p)
                         print("passager supprimer")
                         break
                    else:
                         print("pas de passager avec ce nom dans ce bus")
                         break    

def menu():
     print("1- Ajouter un bus")
     print("2- Ajouter un passager")
     print("3- Afficher les bus")
     print("4- Rechercher un bus")
     print("5- Afficher les passagers d un bus")
     print("6- Supprimer un passager d un bus")
     print("7- Quitter")

def choix():
     Bus=[]
     while True:
          menu()
          c=int(input("Donner votre choix : "))
          if c==1:
               Ajouter_bus(Bus)
          elif c==2:
               Ajouter_passager(Bus)
          elif c==3:
               Afficher_Bus(Bus)
          elif c==4:
               Rechercher_Bus(Bus)
          elif c==5:
               Afficher_passager_Bus(Bus)
          elif c==6:
               supprimer_passager(Bus)
          elif c==7:
               print("Merci d avoir utiliser notre programme")
               break
          else:
               print("choix incorrecte")



     
               

     
                
                      
        
            


def main():
     print("=================================================================================")
     print("                       Bienvenue dans notre programme de gestion de bus           ")
     print("=================================================================================")
     print( "Veuillez choisir une option : ")
    
     choix()

     print("=================================================================================")
     print("                       Merci d avoir utiliser notre programme de gestion de bus     ")  
     print("=================================================================================")

     

if __name__=="__main__":     main()