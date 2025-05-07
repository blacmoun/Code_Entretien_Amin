# 🧠 MindMap CLI

## 💡 Description

MindMap CLI est une application en ligne de commande permettant de créer, visualiser, organiser et sauvegarder des **cartes mentales**.  
Chaque carte est structurée sous forme d’arborescence et limitée à **3 niveaux de profondeur** maximum (racine incluse).

---

## 🚀 Installation

```bash
git clone https://github.com/blacmoun/Code_Entretien_Amin.git
cd mindmap-cli
pip install -r requirements.txt  # S'il y a des dépendances

▶️ Lancer l'application

```bash
python main.py

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
1. Créer une carte
2. Ajouter un nœud
3. Supprimer un nœud
4. Afficher la carte
5. Rechercher un nœud
6. Sauvegarder
7. Charger
8. Quitter
Choix : 1
Nom de la carte : Projet 2025

Choix : 2
Nom du parent : Projet 2025
Nom du nouveau nœud : Backend
Nœud ajouté.

Choix : 2
Nom du parent : Backend
Nom du nouveau nœud : API REST
Nœud ajouté.

Choix : 2
Nom du parent : Backend
Nom du nouveau nœud : Base de données
Nœud ajouté.

Choix : 4
- Projet 2025
  - Backend
    - API REST
    - Base de données

Choix : 5
Nom du nœud à rechercher : Base de données
Projet 2025 > Backend > Base de données

Choix : 6
Carte sauvegardée.

Choix : 8

👨‍💻 Auteur
Ce projet a été réalisé dans le cadre d’un test technique développeur 2025.