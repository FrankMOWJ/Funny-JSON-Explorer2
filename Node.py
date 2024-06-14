
class Node:
    def accept(self):
        pass

class JSONNode(Node):
    def __init__(self, name, value=None, level=0):
        self.name = name
        self.value = value
        self.is_last = False
        self.level = 0
        self.children = []
        self.has_siblings = []
    
    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return self.name + (": " + self.value if self.value else "")
    
    def accept(self, visitor):
        return visitor.visit_json_node(self)
        