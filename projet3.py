def ajouter_chambre(chambres):
     chambre={}
     chambre['numero']=input("Donner le numero de la chambre : ")
     chambre['type']=input("Donner le type de la chambre : ")
     chambre['prix']=input("Donner le prix de la chambre : ")
     chambre['occupe']=False
     chambres.append(chambre)

def afficher_chambres(chambres):
     if len(chambres)==0:
          print("Pas de chambres ")
     else:
          for chambre in chambres:
               print("numero :", chambre['numero'])
               print("type :", chambre['type'])
               print("prix : ", chambre['prix'])
               print("occupe : ", chambre['occupe'])

def rechercher_chambre(chambres):
     
     if len(chambres)==0:
          print("pas de chambres")
     else:
          c=input("les numero de chambre a rechercher ")
          trouver= False
          for chambre in chambres:
               if chambre['numero']==c:
                    trouver=True
                    print("numero :", chambre['numero'])
                    print("type :", chambre['type'])
                    print("prix : ", chambre['prix'])
                    print("occupe : ", chambre['occupe'])
                    break
          if trouver==False:
               print("pas trouver")

def reserver_chambre(chambres):
     if len(chambres)==0:
          print("pas de chambres")
     else:
          c=input("Donner type de chambre que vous voulez : ")
          trouver=False
          for chambre in chambres:
               if chambre['type']==c:
                    if chambre['occupe']==False:
                         chambre['occupe']=True
                         print("chambre reservé avec succes")
                         trouver=True
                         return chambre['numero']
                         
          if trouver==False:    
            print("desoler nous n avons pas ce type de chambre")
            return None
                       
def liberer_chambre(chambres, clients):
     if len(chambres)==0:
          print("pas de chambres")
     else:
          c=input("Donner le numero de chambre que vous voulez liberer : ")
          trouver=False
          for chambre in chambres:
               if chambre['numero']==c:
                    if chambre['occupe']==True:
                         chambre['occupe']=False
                         for client in clients:
                                 if client['numero_chambre']==c:
                                        clients.remove(client)
                         print("chambre liberé avec succes")
                         trouver=True
                         break
          if trouver==False:
                print("desoler nous n avons pas ce numero de chambre")
                      
def afficher_chambres_libres(chambres):
     if len(chambres)==0:
          print("pas de chambres")
     else:
          for chambre in chambres:
               if chambre['occupe']==False:
                    print("numero :", chambre['numero'])
                    print("type :", chambre['type'])
                    print("prix : ", chambre['prix'])
                    print("occupe : ", chambre['occupe'])

def afficher_chambres_occupees(chambres):
     if len(chambres)==0:
          print("pas de chambres")
     else:
          for chambre in chambres:
               if chambre['occupe']==True:
                    print("numero :", chambre['numero'])
                    print("type :", chambre['type'])
                    print("prix : ", chambre['prix'])
                    print("occupe : ", chambre['occupe'])

def recette_totale(chambres):
     if len(chambres)==0:
          print("pas de chambres")
     else:
          total=0
          for chambre in chambres:
               if chambre['occupe']==True:
                    total+=int(chambre['prix'])
          print("la recette totale est : ", total)

def ajouter_client(clients, chambres):
     client={}
     client['nom']=input("Donner le nom du client : ")
     client['prenom']=input("Donner le prenom du client : ")
     client['age']=input("Donner l age du client : ")
     numero_chambre = reserver_chambre(chambres)
     if numero_chambre != None:
        client["numero_chambre"]=numero_chambre
        clients.append(client)
     else:
        print("desoler nous n avons pas de chambre disponible pour ce client")

def afficher_clients(clients):
        if len(clients)==0:
            print("Pas de clients ")
        else:
            for client in clients:
                print("nom :", client['nom'])
                print("prenom :", client['prenom'])
                print("age : ", client['age'])
                print("numero de chambre : ", client['numero_chambre'])

def afficher_clients_chambre(clients):
     if len(clients)==0:
          print("pas de clients")
     else:
          c=input("Donner le numero de chambre dont vous voulez afficher les clients : ")
          trouve = False
          for client in clients:
               if client['numero_chambre']==c:
                    print("nom :", client['nom'])
                    print("prenom :", client['prenom'])
                    print("age : ", client['age'])
                    print("numero de chambre : ", client['numero_chambre'])
                    trouve = True
          if trouve == False:
                    print("desoler nous n avons pas de client dans cette chambre")

def menu():
     print("1- Ajouter une chambre")
     print("2- Afficher les chambres")
     print("3- Rechercher une chambre")
     print("4- Reserver une chambre")
     print("5- Liberer une chambre")
     print("6- Afficher les chambres libres")
     print("7- Afficher les chambres occupées")
     print("8- Recette totale")
     print("9- Ajouter un client")
     print("10- Afficher les clients")
     print("11- Afficher les clients d une chambre")
     print("12- Quitter")

def choix():
     chambres=[]
     clients=[]
     while True:
          menu()
          c=int(input("Donner votre choix : "))
          if c==1:
               ajouter_chambre(chambres)
          elif c==2:
               afficher_chambres(chambres)
          elif c==3:
               rechercher_chambre(chambres)
          elif c==4:
               reserver_chambre(chambres)
          elif c==5:
               liberer_chambre(chambres, clients)
          elif c==6:
               afficher_chambres_libres(chambres)
          elif c==7:
               afficher_chambres_occupees(chambres)
          elif c==8:
               recette_totale(chambres)
          elif c==9:
               ajouter_client(clients, chambres)
          elif c==10:
               afficher_clients(clients)
          elif c==11:
               afficher_clients_chambre(clients)
          elif c==12:
               break

def main():
    print("=========================================================================")
    print("            Bienvenue dans notre systeme de gestion d hotel               ")
    print("=========================================================================")
    print("Veuillez choisir une option : ")
    
    
    choix()
    

    print("=========================================================================")
    print("            Merci d avoir utiliser notre systeme de gestion d hotel         ")
    print("=========================================================================")

if __name__=="__main__":    
 main()