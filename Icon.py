class IconFamily:
    def __init__(self, node_icon="", leaf_icon=""):
        self.node_icon = node_icon
        self.leaf_icon = leaf_icon

    def get_node_icon(self):
        return self.node_icon

    def get_leaf_icon(self):
        return self.leaf_icon
