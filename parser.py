from Node import JSONNode
import copy

class JSONTreeBuilder:
    # 建造者模式
    def build_tree(self, json_obj):
        root = JSONNode("root", level=-1)
        self.parse_object(json_obj, root)
        result = self.pre_order_traversal(root, level=root.level)
        result = result[1:] # remove the root
        return result 

    def parse_object(self, json_obj, parent):
        for key, value in json_obj.items():
            node = JSONNode(key, None if isinstance(value, dict) else value)
            parent.add_child(node)
            if isinstance(value, dict):
                self.parse_object(value, node)

    def pre_order_traversal(self, root, level):
        if root is None:
            return []
        
        result = []
        # result.append((root.name, root.level, root.has_siblings, root.is_last))
        result.append(root)
        for idx, child in enumerate(root.children):
            child.level = level
            if len(child.has_siblings) == 0:
                child.has_siblings = copy.deepcopy(root.has_siblings)
            if idx == len(root.children) - 1:
                child.is_last = True
                child.has_siblings.append(False)
            else :
                child.has_siblings.append(True)
            result.extend(self.pre_order_traversal(child, level+1))
            
        
        return result
    

if __name__ == "__main__":
    import json
    builder = JSONTreeBuilder()
    with open('../test_case.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    result = builder.build_tree(json_data)
    # print(result)