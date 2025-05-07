class Node:
    def __init__(self, name):
        # Initialise un noeud avec un nom et une liste d'enfants vide
        self.name = name
        self.children = []

    def add_child(self, child):
        # Ajoute un noeud enfant
        self.children.append(child)
        return True

    def depth(self, level=0):
        # Calcule la profondeur maximale du sous-arbre
        if not self.children:
            return level
        return max(child.depth(level + 1) for child in self.children)

    def find(self, name, path=None):
        # Recherche recursive d'un noeud et retourne son chemin depuis la racine
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
        # Supprime un noeud enfant par nom (et ses enfants)
        for i, child in enumerate(self.children):
            if child.name == name:
                del self.children[i]
                return True
            if child.remove(name):
                return True
        return False

    def to_dict(self):
        # Transforme le noeud et ses enfants en dictionnaire (pour sauvegarde)
        return {
            "name": self.name,
            "children": [child.to_dict() for child in self.children]
        }

    @staticmethod
    def from_dict(data):
        # Cree un noeud depuis un dictionnaire (chargement JSON)
        node = Node(data["name"])
        node.children = [Node.from_dict(child) for child in data.get("children", [])]
        return node

    def display(self, indent=0):
        # Affiche l'arbre avec indentation selon le niveau
        print("  " * indent + "- " + self.name)
        for child in self.children:
            child.display(indent + 1)
