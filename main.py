# main.py

def print_menu():
    print("\nCommandes :")
    print("1. Créer une carte")
    print("2. Ajouter un nœud")
    print("3. Sauvegarder")
    print("4. Charger")
    print("5. Quitter")

def main():
    mindmap = None

    while True:
        print_menu()
        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom de la carte : ")

        elif choix == "2":
            if not mindmap:
                print("Créez d'abord une carte.")
                continue
            parent = input("Nom du parent : ")
            enfant = input("Nom du nouveau nœud : ")
            if mindmap.add_node(parent, enfant):
                print("Nœud ajouté.")
            else:
                print("Erreur : parent introuvable ou profondeur maximale atteinte.")

        elif choix == "3":
            if not mindmap:
                print("Aucune carte à sauvegarder.")
                continue
            print("Carte sauvegardée.")

        elif choix == "4":
            print("Carte chargée.")

        elif choix == "5":
            break

        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    main()
