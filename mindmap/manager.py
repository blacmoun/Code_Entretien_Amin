from .models import Node

class MindMapManager:
    def __init__(self, root_name):
        # Cree une carte mentale avec un noeud racine
        self.root = Node(root_name)

    def add_node(self, parent_name, child_name):
        # Ajoute un noeud enfant a un noeud parent existant
        # Verifie que le parent existe, que le nom est unique,
        # et que le parent n'est pas deja au niveau 2 (max autorise)

        parent = self._find_node(self.root, parent_name)
        if not parent:
            print("Erreur : parent introuvable.")
            return False

        if self._find_node(self.root, child_name):
            print("Erreur : un noeud avec ce nom existe deja.")
            return False

        level = self._get_node_level(parent_name)
        if level is not None and level >= 2:
            print("Erreur : profondeur maximale atteinte.")
            return False

        parent.add_child(Node(child_name))
        print("Noeud ajoute.")
        return True

    def remove_node(self, name):
        # Supprime un noeud sauf si c'est la racine
        if self.root.name == name:
            return False

        # Recherche recursive dans les enfants pour supprimer
        for i, child in enumerate(self.root.children):
            if child.name == name:
                del self.root.children[i]
                return True
            if child.remove(name):
                return True
        return False

    def search(self, name):
        # Recherche un noeud par nom et retourne le chemin
        return self.root.find(name)

    def display(self):
        # Affiche la carte sous forme d'arborescence
        self.root.display()

    def to_dict(self):
        # Convertit l'arbre en dictionnaire (pour JSON)
        return self.root.to_dict()

    @staticmethod
    def from_dict(data):
        # Cree une carte a partir d'un dictionnaire JSON
        manager = MindMapManager(data["name"])
        manager.root = Node.from_dict(data)
        return manager

    def _find_node(self, node, name):
        # Recherche recursive d'un noeud par nom
        if node.name == name:
            return node
        for child in node.children:
            found = self._find_node(child, name)
            if found:
                return found
        return None

    def _get_node_level(self, target_name, node=None, level=0):
        # Determine le niveau du noeud dans l'arborescence
        if node is None:
            node = self.root
        if node.name == target_name:
            return level
        for child in node.children:
            result = self._get_node_level(target_name, child, level + 1)
            if result is not None:
                return result
        return None
