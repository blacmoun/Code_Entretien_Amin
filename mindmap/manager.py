# -*- coding: utf-8 -*-
from .models import Node

class MindMapManager:
    def __init__(self, root_name):
        self.root = Node(root_name)

    def add_node(self, parent_name, child_name):
        parent = self._find_node(self.root, parent_name)
        if parent:
            level = self._get_node_level(parent_name)
            if level is not None and level < 2:  # max 3 niveaux (racine + 2)
                return parent.add_child(Node(child_name))
        return False

    def remove_node(self, name):
        if self.root.name == name:
            return False  # On ne peut pas supprimer la racine
        return self.root.remove(name)

    def search(self, name):
        return self.root.find(name)

    def display(self):
        self.root.display()

    def to_dict(self):
        return self.root.to_dict()

    @staticmethod
    def from_dict(data):
        manager = MindMapManager(data["name"])
        manager.root = Node.from_dict(data)
        return manager

    def _find_node(self, node, name):
        if node.name == name:
            return node
        for child in node.children:
            found = self._find_node(child, name)
            if found:
                return found
        return None

    def _get_node_level(self, target_name, node=None, level=0):
        if node is None:
            node = self.root
        if node.name == target_name:
            return level
        for child in node.children:
            result = self._get_node_level(target_name, child, level + 1)
            if result is not None:
                return result
        return None
