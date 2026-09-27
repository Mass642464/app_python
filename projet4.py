
import json

def charger(fichier='banque.json'):
    try:
        with open(fichier,encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
       
def Sauvegarder(Banque, fichier='banque.json'):

    with open( fichier ,'w',encoding='utf-8') as f:
        json.dump(Banque,f,ensure_ascii=False, indent=2)
    print("Donne sauvegarder avec succes ")


def saisie_personne():
    matricule=input("Donne votre Matricule ")
    nom=input("Donner Votre Nom")
    prenom=input("Donner Votre Prenom")

    return {'matricule':matricule, 'nom':nom, 'prenom':prenom}

def afficher_un_employe(employe):
    print(f"Matricule: {employe['matricule']}")
    print(f"Nom: {employe['nom']}")
    print(f"Prenom: {employe['prenom']}")
    print(f"Poste: {employe['poste']}")

def existe(Banque):
    return Banque != None

def employes_existe(Banque , employe):
  if existe(Banque)==True:
      for Employe in Banque['Employes']: 
          if Employe['matricule']==employe['matricule']:
              return True
      return False
          
      

def Creer_Banque():
    Banque={}
    Nom_Banque= input("Donnez le Nom de Votre Baonque ")
    Directeur = saisie_personne()
    Employes=[]
    Employes.append({'matricule':Directeur['matricule'], 'nom':Directeur['nom'], 'prenom':Directeur['prenom'], 'poste':'Directeur'})
    Banque['Nom_Banque']=Nom_Banque
    Banque['Directeur']=Directeur   
    Banque['Employes']=Employes
    Banque['clients']=[]
    return Banque

def Ajouter_Employe(Banque):
  if existe(Banque)==True:
    Employe=saisie_personne()
    Employe['poste']=input("Donner le poste de l employe ")
    if  employes_existe(Banque, Employe) == False:
     Banque['Employes'].append(Employe)
  else:
     print("La Banque n existe pas")

def Afficher_Employes(Banque):
    if existe(Banque)==True:
        for Employe in Banque['Employes']:
            afficher_un_employe(Employe)
    else:
         print("La Banque n existe pas")

def Rechercher_Employe(Banque):
    if existe(Banque)==True:
        matricule=input("Donner le matricule de l employe a rechercher ")
        for Employe in Banque['Employes']:
            if Employe['matricule']==matricule:
                afficher_un_employe(Employe)
                break
        else:
            print("L employe n existe pas")
    else:
         print("La Banque n existe pas")

def creer_compte(banque):
   while True:
    numero_compte = input("Numéro de compte : ")
    deja_pris = any(
        cl['compte']['numero_compte'] == numero_compte
        for cl in banque['clients']
    )
    if not deja_pris:
        break
    print("Ce numéro existe déjà, essayez un autre.")

   solde = float(input("Solde initial : "))
   mot_de_passe = input("Mot de passe : ")
   return {'numero_compte': numero_compte, 'solde': solde, 'historique': [], 'mot_de_passe': mot_de_passe}

def rechercher_client(Banque ):
    if existe(Banque):
        Matricule=input("Donner le matricule du client a rechercher ")
        for client in Banque['clients']:
            if client['matricule']==Matricule:
                return client
        else:
            print("Le client n existe pas")
            return None


def Ajouter_Client(Banque):
    if existe(Banque)==True:
        Client=saisie_personne()
        Client['compte']=creer_compte(Banque)
        Banque['clients'].append(Client)
    else:
         print("La Banque n existe pas")

def depot(Banque) :
    if existe(Banque):
        client =rechercher_client(Banque) 
        if client :
            solde=float(input("Donner le montant a deposer "))
            client['compte']['solde'] += solde
            client['compte']['historique'].append(('depot', solde))
            print("Le depot a ete effectue avec succes")
        else:
            print("Le client n existe pas")
    else:
         print("La Banque n existe pas")

def retrait(Banque) :
    if existe(Banque):
        client =rechercher_client(Banque) 
        if client :
           solde=float(input("Donner le montant a retirer "))
           essaie=3
           while True:
               mot_de_passe=input("Donner votre mot de passe pour confirmer le retrait ")
               if mot_de_passe==client['compte']['mot_de_passe']:
                    break
               essaie -= 1
               if essaie == 0:
                   print("Trop de tentatives, retrait annulé")
                   return
           if solde <= client['compte']['solde']:
                client['compte']['solde'] -= solde
                client['compte']['historique'].append(('retrait', solde))
                print("Le retrait a ete effectue avec succes")
           else:
                print("Solde insuffisant")
        else:
            print("Le client n existe pas")
    else:
         print("La Banque n existe pas")

def tranfert(Banque) :
    if existe(Banque):
        client =rechercher_client(Banque) 
        if client :
           solde=float(input("Donner le montant a transferer "))
           numero_compte_dest=input("Donner le numero de compte du destinataire ")
           essaie=3
           while True:
               mot_de_passe=input("Donner votre mot de passe pour confirmer le transfert ")
               if mot_de_passe==client['compte']['mot_de_passe']:
                    break
               essaie -= 1
               if essaie == 0:
                   print("Trop de tentatives, transfert annulé")
                   return
           if solde <= client['compte']['solde']:
                for client_dest in Banque['clients']:
                    if client_dest['compte']['numero_compte']==numero_compte_dest:
                        client['compte']['solde'] -= solde
                        client_dest['compte']['solde'] += solde
                        client['compte']['historique'].append(('transfert', solde, numero_compte_dest))
                        client_dest['compte']['historique'].append(('reception', solde, client['compte']['numero_compte']))
                        print("Le transfert a ete effectue avec succes")
                        break
                else:
                    print("Le numero de compte du destinataire n existe pas")
           else:
                print("Solde insuffisant")
        else:
            print("Le client n existe pas")
    else:
         print("La Banque n existe pas")

def menu():
    print("1- Creer une banque")
    print("2- Ajouter un employe")
    print("3- Afficher les employes")
    print("4- Rechercher un employe")
    print("5- Ajouter un client")
    print("6- Depot")
    print("7- Retrait")
    print("8- Transfert")

def choix():


    try:
       Banque =charger('banque.json')
       while True:
                menu()
                c=int(input("Donner votre choix : "))
                if c==1:
                    Banque =Creer_Banque()
                elif c==2:
                    Ajouter_Employe(Banque)
                elif c==3:
                    Afficher_Employes(Banque)
                elif c==4:
                    Rechercher_Employe(Banque)
                elif c==5:
                    Ajouter_Client(Banque)
                elif c==6:
                    depot(Banque)
                elif c==7:
                    retrait(Banque)
                elif c==8:
                    tranfert(Banque)

    except ValueError as error:
        print(error)
    Sauvegarder(Banque,'banque.json')

def main():
    print("=========================================================================")
    print("            Bienvenue dans notre systeme de gestion de Votre Banque              ")
    print("=========================================================================")
    print("Veuillez choisir une option : ")
    
    
    choix()
    

    print("=========================================================================")
    print("            Merci d avoir utiliser notre systeme          ")
    print("=========================================================================")

if __name__=="__main__":    
 main()

      
