from .models import Node

class MindMapManager:
    def __init__(self, root_name):
        # Cree une nouvelle carte mentale avec un noeud racine
        self.root = Node(root_name)

    def add_node(self, parent_name, child_name):
        # Ajoute un noeud enfant a un noeud parent si la profondeur max n'est pas atteinte
        parent = self._find_node(self.root, parent_name)
        if parent:
            level = self._get_node_level(parent_name)
            if level is not None and level < 2:  # max 3 niveaux (0, 1, 2)
                return parent.add_child(Node(child_name))
        return False

    def remove_node(self, name):
        # Supprime un noeud par nom, sauf si c'est la racine
        if self.root.name == name:
            return False
        return self.root.remove(name)

    def search(self, name):
        # Recherche un noeud par nom et retourne son chemin depuis la racine
        return self.root.find(name)

    def display(self):
        # Affiche la carte mentale sous forme d'arbre
        self.root.display()

    def to_dict(self):
        # Convertit la carte en dictionnaire (pour sauvegarde JSON)
        return self.root.to_dict()

    @staticmethod
    def from_dict(data):
        # Construit une carte mentale a partir d'un dictionnaire
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
        # Determine le niveau d'un noeud (profondeur depuis la racine)
        if node is None:
            node = self.root
        if node.name == target_name:
            return level
        for child in node.children:
            result = self._get_node_level(target_name, child, level + 1)
            if result is not None:
                return result
        return None
