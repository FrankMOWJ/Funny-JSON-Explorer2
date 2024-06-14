from Visitor import *
from Node import *
from Iterator import *
from parser import *
from Icon import *
import json
import argparse
def main():
    # python main.py -c ./config/config.json
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-c', '--config', type=str, required=True, help='Path to configuration file')
    
    args = parser.parse_args()

    with open(args.config, 'r', encoding='utf-8') as file:
        config = json.load(file)

    with open(config['json_file'], 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    # Icon 
    style = config['style']
    node_icon = config['icon']['node']
    leaf_icon = config['icon']['leaf']
    icons = IconFamily(node_icon=node_icon, leaf_icon=leaf_icon)

    builder = JSONTreeBuilder()
    json_data = builder.build_tree(json_data)
    iterator = JSONIteratorCollection().create_Iterator(json_data)
    visitor = TreeVisitor() if style == 'tree' else RectangleVisitor()
    visitor.set_icons(icons)

    buffer = []
    while iterator.hasNext():
        nextNode = iterator.next()
        if isinstance(nextNode, JSONNode):
            buffer.append(nextNode.accept(visitor))
        else:
            print(nextNode)
        
    # post-process the buffer 
    visitor.post_precess_buffer(buffer)

if __name__ == "__main__":
    main()