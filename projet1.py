def main():
 
 
 Boutique = []
 print("===================================================================================")
 print("                     Bienvenu Dans le Menu De  Votre Boutique                      ")
 print("===================================================================================")
 while True:
    print("---------------------------------------------------------------------------------")
    print("                                      MENU                                       ")
    print("---------------------------------------------------------------------------------")
    print("                           +                           ")
    print("1 - Ajouter un Produit" )
    print("2 - Afficher ")
    print("3 - Rechercher un Produit")
    print("4 - Modfier un Produit")
    print("5 - Supprimer un Produit")
    print("6 - Vendre ")
    print("7 - QUITTER  ")
    
    choix=input("   Vellez Choisir un Numero  :")

    if choix=="1":
      nom = input("donner le nom du produit : ")
      prix = int(input("donner le prix du produit : "))
      quantite = int(input("donner la quantite du produit : "))
      Boutique.append({'nom':nom , 'prix':prix, 'quantite': quantite})

    elif choix=="2":
      while True:
        print("---------------------------------------------------------------------------------")
        print("                         MENU AFFICHAGE                                       ")
        print("---------------------------------------------------------------------------------")
        print("                           +                           ")
        print("1 - Afficher un Produit" )
        print("2 - Afficher tous les produits ")
        print("3 - Afficher la valeur totale du stock")
        print("4 - QUITTER ")

        choix=input("   Vellez Choisir un Numero  ")

        if choix=="1":
          p = input("Veillez Donner le Nom du Produit Que vous Vouliez Afficher :")
          for produit in Boutique :
            if p==produit['nom'] :
              print("Nom :", produit['nom'])
              print("Prix :", produit['prix'])
              print("Quantite :", produit['quantite'])
        elif choix=="2":
          for produit in Boutique :
              print("Nom :", produit['nom'])
              print("Prix :", produit['prix'])
              print("Quantite :", produit['quantite'])
              print("-------------------------------------")
        elif choix=="3":
          valeur= 0
          for produit in Boutique :
             valeur+= produit['prix']*produit['quantite']
          print("La valeur Totale du Stock est : ", valeur)
        elif choix=="4": break
    elif choix=="3":
      p=input("Veiillez Donner le Produit a Rechercher :")
      for produit in Boutique :
        if p==produit['nom']:
              print("Nom :", produit['nom'])
              print("Prix :", produit['prix'])
              print("Quantite :", produit['quantite'])
              print("-------------------------------------")

    elif choix=="4":
       
       p=input("Veiillez Donner le Produit a Modifier :")
       for produit in Boutique:
          if p==produit['nom']:
             print("Voici la quantie Actuelle : ", produit['quantite'])
             valeur=input("Donner La nouvelle Quantite :")
             produit['quantite']=int(valeur)
    elif choix=="5": 

         p=input("Veiillez Donner le Produit a Supprimer :")
         for produit in Boutique:
          if p==produit['nom']:
              Boutique.remove(produit) # remove c est pour supprimer un element d une liste
              print("Produit Supprimmer Avec Succes : " )

    elif choix=="6":
            p=input("Veiillez Donner le Produit Vendu :")
            
            for produit in Boutique:
              if p==produit['nom']:
                q=input("Veiillez Donner le Quantite Vendu :")
                if int(q) > produit['quantite']:
                   print("la quantite est insuffissante ")
                else:
                   produit['quantite']-= int(q) 
    else : break

            
    

if __name__ == "__main__":
 main()