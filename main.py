from mindmap.manager import MindMapManager
from mindmap.storage import save_mindmap, load_mindmap, list_mindmaps

# Affiche le menu principal avec les choix possibles
def print_menu():
    print("\nCommandes :")
    print("1. Creer une carte")
    print("2. Ajouter un noeud")
    print("3. Supprimer un noeud")
    print("4. Afficher la carte")
    print("5. Rechercher un noeud")
    print("6. Sauvegarder")
    print("7. Charger")
    print("8. Quitter")
    print("9. Lister les cartes sauvegardees")

# Fonction principale du programme
def main():
    mindmap = None
    nom_carte = None

    while True:
        print_menu()
        choix = input("Choix : ")

        # Creation d'une nouvelle carte
        if choix == "1":
            nom = input("Nom de la carte : ")
            mindmap = MindMapManager(nom)
            nom_carte = nom

        # Ajout d'un noeud
        elif choix == "2":
            if not mindmap:
                print("Veuillez d'abord creer une carte.")
                continue
            parent = input("Nom du parent : ")
            enfant = input("Nom du nouveau noeud : ")
            if mindmap.add_node(parent, enfant):
                print("Noeud ajoute.")
            else:
                print("Erreur : parent introuvable ou profondeur max atteinte.")

        # Suppression d'un noeud
        elif choix == "3":
            if not mindmap:
                print("Veuillez d'abord creer une carte.")
                continue
            nom = input("Nom du noeud a supprimer : ")
            if mindmap.remove_node(nom):
                print("Noeud supprime.")
            else:
                print("Erreur : noeud introuvable.")

        # Affichage de la carte
        elif choix == "4":
            if not mindmap:
                print("Veuillez d'abord creer une carte.")
                continue
            mindmap.display()

        # Recherche d'un noeud
        elif choix == "5":
            if not mindmap:
                print("Veuillez d'abord creer une carte.")
                continue
            nom = input("Nom du noeud a rechercher : ")
            chemin = mindmap.search(nom)
            if chemin:
                print(" > ".join(chemin))
            else:
                print("Noeud introuvable.")

        # Sauvegarde
        elif choix == "6":
            if not mindmap:
                print("Aucune carte a sauvegarder.")
                continue
            nom = input("Nom du fichier de sauvegarde : ")
            save_mindmap(mindmap, nom)
            print("Carte sauvegardee.")

        # Chargement
        elif choix == "7":
            cartes = list_mindmaps()
            if not cartes:
                print("Aucune carte trouvee.")
                continue
            print("Cartes disponibles :")
            for c in cartes:
                print("-", c)
            nom = input("Nom de la carte a charger : ")
            mindmap = load_mindmap(nom)
            if mindmap:
                nom_carte = nom
                print("Carte chargee.")
            else:
                print("Erreur : carte introuvable.")

        # Quitter
        elif choix == "8":
            print("Au revoir.")
            break

        # Liste des cartes sauvegardees
        elif choix == "9":
            cartes = list_mindmaps()
            if cartes:
                print("Cartes disponibles :")
                for c in cartes:
                    print("-", c)
            else:
                print("Aucune carte sauvegardee.")

        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    main()
