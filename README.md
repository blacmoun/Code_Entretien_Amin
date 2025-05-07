# 🧠 MindMap CLI

## 💡 Description

MindMap CLI est une application en ligne de commande permettant de créer, visualiser, organiser et sauvegarder des **cartes mentales**.  
Chaque carte est structurée sous forme d’arborescence et limitée à **3 niveaux de profondeur** maximum (racine incluse).

---

## 👨‍💻 Auteur 
Ce projet a été réalisé par moi-même dans le cadre d’un test technique développeur 2025 et avec l'aide de chatgpt.

## 🚀 Installation

```bash
git clone https://github.com/blacmoun/Code_Entretien_Amin.git
cd mindmap-cli
```

▶️ Lancer l'application
```bash
python main.py
```
Commandes :
1. Créer une carte
2. Ajouter un nœud
3. Supprimer un nœud
4. Afficher la carte
5. Rechercher un nœud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardées


$ python main.py

✅ Exemple d'utilisation (copier/coller CLI)

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 1
Nom de la carte : exemple

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 2
Nom du parent : exemple
Nom du nouveau noeud : code
Noeud ajoute.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 4
- exemple
  - code

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : code
Commande inconnue.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : python
Commande inconnue.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 2
Nom du parent : exemple
Nom du nouveau noeud : sport
Noeud ajoute.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 2
Nom du parent : sport
Nom du nouveau noeud : foot
Noeud ajoute.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 4
- exemple
  - code
  - sport
    - foot

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 2
Nom du parent : foot
Nom du nouveau noeud : ronaldo
Erreur : profondeur maximale atteinte.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 4
- exemple
  - code
  - sport
    - foot

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 3
Nom du noeud a supprimer : sport
Noeud supprime.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 4
- exemple
  - code

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 2
Nom du parent : code
Nom du nouveau noeud : python
Noeud ajoute.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 4
- exemple
  - code
    - python

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 5
Nom du noeud a rechercher : python
exemple > code > python

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 6
Nom du fichier de sauvegarde : exemple
Carte sauvegardee.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 9
Cartes disponibles :
- blacmoun
- exemple
- teste

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 7
Cartes disponibles :
- blacmoun
- exemple
- teste
Nom de la carte a charger : teste
Carte chargee.

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 4
- 7
  - 6
    - 5
    - 4
  - 6.5

Commandes :
1. Creer une carte
2. Ajouter un noeud
3. Supprimer un noeud
4. Afficher la carte
5. Rechercher un noeud
6. Sauvegarder
7. Charger
8. Quitter
9. Lister les cartes sauvegardees
Choix : 8

👨‍💻 Auteur
Ce projet a été réalisé par moi-même dans le cadre d’un test technique développeur 2025 et avec l'aide de chatgpt.
