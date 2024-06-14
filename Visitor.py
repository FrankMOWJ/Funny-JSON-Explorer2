class Visitor:
    def __init__(self):
        self.icons = None
    def visit_json_node(self, node):
        pass

    def get_indent(self, level, has_siblings):
        pass

    def set_icons(self, icon):
        self.icons = icon

class TreeVisitor(Visitor):
    def visit_json_node(self, node):
        # 使用Tree的模式进行渲染
        level = node.level
        has_siblings = node.has_siblings
        indent = self.get_indent(level, has_siblings)
        branch_char = '└─' if node.is_last else '├─'
        border = indent + branch_char +  (self.icons.get_leaf_icon() if len(node.children) == 0 else self.icons.get_node_icon()) + str(node)
        return border
       

    def get_indent(self, level, has_siblings):
        indent = ''
        for i in range(level):
            # 上一级之后有同级子节点，则使用分支字符
            if has_siblings[i]:
                indent += '│  '
            else:
                indent += '   '
        return indent
    
    def post_precess_buffer(self, buffer):
        for i in range(len(buffer)):
            print(buffer[i])


class RectangleVisitor(Visitor):
    def visit_json_node(self, node):
        # 使用Rectangle的模式进行渲染
        level = node.level
        # 先缓存起来
        border = self.get_indent(level) + (self.icons.get_leaf_icon() if len(node.children) == 0 else self.icons.get_node_icon())
        border += str(node) + " " 
        border += "─" * (38 - len(border) ) + '─┤'     
        return border

    def get_indent(self, level):
        indent = ''
        indent += '│  ' * (level)
        indent += '├─ '
        return indent
    
    def post_precess_buffer(self, buffer):
        for i in range(len(buffer)):
            if i == 0:
                buffer[i] = buffer[i].replace('├─ ', '┌─ ')
                buffer[i] = buffer[i].replace('─┤', '─┐')
            if i == len(buffer) - 1:
                buffer[i] = buffer[i].replace(' ├─ ', '└─')
                buffer[i] = buffer[i].replace('─┤', '')
                buffer[i] = buffer[i].replace('│', '└─')
                buffer[i] += "─" * (38 - len(buffer[i]) ) + '─┘'
            print(buffer[i])

