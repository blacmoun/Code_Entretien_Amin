class Node:
    def __init__(self, name):
        # Cree un noeud avec un nom
        self.name = name
        self.children = []

    def add_child(self, child):
        # Ajoute un enfant si la profondeur max n'est pas depassee
        if self.depth() >= 2:
            return False
        self.children.append(child)
        return True

    def depth(self, level=0):
        # Calcule la profondeur du sous-arbre
        if not self.children:
            return level
        return max(child.depth(level + 1) for child in self.children)

    def find(self, name, path=None):
        # Recherche un noeud par nom et retourne son chemin
        if path is None:
            path = [self.name]
        if self.name == name:
            return path
        for child in self.children:
            result = child.find(name, path + [child.name])
            if result:
                return result
        return None

    def remove(self, name):
        # Supprime un enfant du noeud (et ses sous-noeuds)
        for i, child in enumerate(self.children):
            if child.name == name:
                del self.children[i]
                return True
            if child.remove(name):
                return True
        return False

    def to_dict(self):
        # Transforme le noeud en dictionnaire (pour JSON)
        return {
            "name": self.name,
            "children": [child.to_dict() for child in self.children]
        }

    @staticmethod
    def from_dict(data):
        # Cree un noeud a partir d'un dictionnaire
        node = Node(data["name"])
        node.children = [Node.from_dict(child) for child in data.get("children", [])]
        return node

    def display(self, indent=0):
        # Affiche l'arbre sous forme textuelle avec indentation
        print("  " * indent + "- " + self.name)
        for child in self.children:
            child.display(indent + 1)
