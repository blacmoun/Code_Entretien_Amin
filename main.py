from mindmap.manager import MindMapManager
from mindmap.storage import save_mindmap, load_mindmap, list_mindmaps

def print_menu():
    print("\nCommandes :")
    print("1. Créer une carte")
    print("2. Ajouter un nœud")
    print("3. Supprimer un nœud")
    print("4. Afficher la carte")
    print("5. Rechercher un nœud")
    print("6. Sauvegarder")
    print("7. Charger")
    print("8. Quitter")
    print("9. Lister les cartes sauvegardées")  
def main():
    mindmap = None
    nom_carte = None

    while True:
        print_menu()
        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom de la carte : ")
            mindmap = MindMapManager(nom)
            nom_carte = nom

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
                print("Créez d'abord une carte.")
                continue
            nom = input("Nom du nœud à supprimer : ")
            if mindmap.remove_node(nom):
                print("Nœud supprimé.")
            else:
                print("Nœud introuvable ou suppression impossible.")

        elif choix == "4":
            if not mindmap:
                print("Créez d'abord une carte.")
                continue
            mindmap.display()

        elif choix == "5":
            if not mindmap:
                print("Créez d'abord une carte.")
                continue
            nom = input("Nom du nœud à rechercher : ")
            chemin = mindmap.search(nom)
            if chemin:
                print(" > ".join(chemin))
            else:
                print("Nœud introuvable.")

        elif choix == "6":
            if not mindmap:
                print("Aucune carte à sauvegarder.")
                continue
            nom = input("Nom du fichier de sauvegarde : ")
            save_mindmap(mindmap, nom)
            print(f"Carte '{nom}' sauvegardée.")

        elif choix == "7":
            cartes = list_mindmaps()
            if not cartes:
                print("Aucune carte trouvée.")
                continue
            print("Cartes disponibles :")
            for c in cartes:
                print("-", c)
            nom = input("Nom de la carte à charger : ")
            mindmap = load_mindmap(nom)
            if mindmap:
                nom_carte = nom
                print("Carte chargée.")
            else:
                print("Erreur : carte introuvable.")

        elif choix == "8":
            print("Au revoir !")
            break

        elif choix == "9":
            cartes = list_mindmaps()
            if cartes:
                print("Cartes disponibles :")
                for c in cartes:
                    print("-", c)
            else:
                print("Aucune carte sauvegardée.")

        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    main()
