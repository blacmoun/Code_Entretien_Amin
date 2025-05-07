class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        if self.depth() >= 2:
            return False
        self.children.append(child)
        return True

    def depth(self, level=0):
        if not self.children:
            return level
        return max(child.depth(level + 1) for child in self.children)

    def find(self, name, path=None):
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
        for i, child in enumerate(self.children):
            if child.name == name:
                del self.children[i]
                return True
            if child.remove(name):
                return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "children": [child.to_dict() for child in self.children]
        }

    @staticmethod
    def from_dict(data):
        node = Node(data["name"])
        node.children = [Node.from_dict(child) for child in data.get("children", [])]
        return node

    def display(self, indent=0):
        print("  " * indent + "- " + self.name)
        for child in self.children:
            child.display(indent + 1)
