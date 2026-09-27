import json
class Plat:
    def __init__(self, id , nom , prix):
        self.id=id
        self.nom=nom
        self.prix=prix

    def __str__(self):
        return f"id={self.id}-nom={self.nom}-prix={self.prix}"
    
    def to_dict(self):
        return{'id':self.id,'nom':self.nom,'prix':self.prix}
    
    @staticmethod
    def from_dict(dic):
        return Plat(dic['id'],dic['nom'],dic['prix'] )
    

class Client:
    def __init__(self, id , nom ):
        self.id=id
        self.nom=nom

    def __str__(self):
        return f"id={self.id}-nom={self.nom}"
   
    def to_dict(self):
        return{'id':self.id,'nom':self.nom}
    
    @staticmethod
    def from_dict(dic):
        return Client(dic['id'],dic['nom'])
    

class Commande:
    def __init__(self, id, client  ):
        self.id=id
        self.client=client
        self.plat=[]
    
    def ajouter_plat(self , plat):
        self.plat.append(plat)

    def calculer_total(self):
        sum=0
        for plat in self.plat:
            sum+=plat.prix
        return sum
    def __str__(self):
        return f"commande : {self.id} \n client : {self.client} \n {self.plat} \n Total : {self.calculer_total()}"
    
    def to_dict(self):
        p=[]
        for plat in self.plat:
            p.append(plat.to_dict())
        return {'id':self.id , 'client': self.client, 'plat':p}
    
    @staticmethod
    def from_dict(dic):
        client = Client.from_dict(dic['client'])
        commande = Commande(dic['id'], client)
        for plat_dic in dic.get('plat', []):
            commande.ajouter_plat(Plat.from_dict(plat_dic))
        return commande

class Restaurant:
    def __init__(self):
        self.plat=[]
        self.client=[]
        self.commande=[]

    def ajouter_plat(self , plat):
        self.plat.append(plat)

    def ajouter_client(self, client):
        self.client.append(client)

    def creer_commande(self , commande):
        self.commande.append(commande)

    def rechercher_plat(self , id):
        for plat in self.plat:
            if id == plat.id:
                return plat
        return None  
    
    def rechercher_client(self , id):
        for client in self.client:
            if id == client.id:
                return client
        return None  


    def to_dict(self):
        p=[]
        c=[]
        com=[]
        for client in self.client:
            c.append(client.to_dict())
        for plat in self.plat:
            p.append(plat.to_dict())
        for commande in self.commande:
            com.append(commande.to_dict())

        return {'plat':p , 'client': c, 'commande ': com} 

    @staticmethod
    def from_dict(dic):
        restaurant = Restaurant()
        for plat_dic in dic.get('plat', []):
            restaurant.ajouter_plat(Plat.from_dict(plat_dic))
        for client_dic in dic.get('client', []):
            restaurant.ajouter_client(Client.from_dict(client_dic))
        for commande_dic in dic.get('commande', []):
            restaurant.creer_commande(Commande.from_dict(commande_dic))
        return restaurant    
    
    def sauvegarder(self):
        try :
            with open("restaurant.json", 'w') as f:
                json.dump(  self.to_dict(),f, ensure_ascii=False, indent=4)
        except  FileNotFoundError :
            print("erreur")
    
    def charger(self):
        try :
            with open("restaurant.json", 'r') as f:
                 
                 donnees = json.load(f)
                 restaurant = Restaurant.from_dict(donnees)
                 self.plat = restaurant.plat
                 self.client = restaurant.client
                 self.commande = restaurant.commande
                 return True
        except  FileNotFoundError :
            print("erreur")

def afficher_menu():
    print('\n=== Menu Restaurant ===')
    print('1. Ajouter un plat')
    print('2. Ajouter un client')
    print('3. Créer une commande')
    print('4. Afficher les plats')
    print('5. Afficher les clients')
    print('6. Afficher les commandes')
    print('7. Sauvegarder')
    print('8. Charger')
    print('0. Quitter')


def saisir_entier(message):
    while True:
        valeur = input(message).strip()
        if valeur.isdigit():
            return int(valeur)
        print('Veuillez entrer un nombre entier valide.')


def main():
    restaurant = Restaurant()
    restaurant.charger()

    while True:
        afficher_menu()
        choix = input('Votre choix : ').strip()

        if choix == '1':
            id_plat = input('ID du plat : ').strip()
            nom = input('Nom du plat : ').strip()
            prix = saisir_entier('Prix du plat : ')
            restaurant.ajouter_plat(Plat(id_plat, nom, prix))
            print('Plat ajouté.')

        elif choix == '2':
            id_client = input('ID du client : ').strip()
            nom = input('Nom du client : ').strip()
            restaurant.ajouter_client(Client(id_client, nom))
            print('Client ajouté.')

        elif choix == '3':
            id_commande = input('ID de la commande : ').strip()
            id_client = input('ID du client pour cette commande : ').strip()
            client = restaurant.rechercher_client(id_client)
            if client is None:
                print('Client introuvable. Créez d\u2019abord le client.')
                continue
            commande = Commande(id_commande, client)
            while True:
                id_plat = input('ID du plat à ajouter (vide pour terminer) : ').strip()
                if not id_plat:
                    break
                plat = restaurant.rechercher_plat(id_plat)
                if plat is None:
                    print('Plat introuvable.')
                else:
                    commande.ajouter_plat(plat)
                    print(f'Plat ajouté : {plat.nom}')
            restaurant.creer_commande(commande)
            print('Commande créée.')

        elif choix == '4':
            print('\n--- Plats ---')
            for plat in restaurant.plat:
                print(plat)

        elif choix == '5':
            print('\n--- Clients ---')
            for client in restaurant.client:
                print(client)

        elif choix == '6':
            print('\n--- Commandes ---')
            for commande in restaurant.commande:
                print(commande)
                print('---')

        elif choix == '7':
            restaurant.sauvegarder()
            print('Sauvegarde terminée.')

        elif choix == '8':
            if restaurant.charger():
                print('Chargement terminé.')

        elif choix == '0':
            print('Au revoir !')
            break

        else:
            print('Choix invalide, réessayez.')


if __name__ == '__main__':
    main()
