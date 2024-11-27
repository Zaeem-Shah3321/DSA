class GraphNode:
    def __init__(self, value):
        self.value = value
        self.children = []
class EquationGraph:
    def __init__(self, prefix_expression):
        self.prefix_expression = prefix_expression
        self.root = None
    def build_graph(self):
        stack = []
        for token in reversed(self.prefix_expression):
            node = GraphNode(token)
            if token in "+-*/=":  
                if len(stack) < 2:
                    raise ValueError("Invalid prefix expression")
                node.children.append(stack.pop())
                node.children.append(stack.pop())
            stack.append(node)
        if len(stack) != 1:
            raise ValueError("Invalid prefix expression")
        self.root = stack.pop()

    def display_graph(self, node, level=0):
        if node:
            print("  " * level + str(node.value))
            for child in node.children:
                self.display_graph(child, level + 1)
def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '=': 0}
    stack, output = [], []
    tokens = tokenize(expression)
    for token in reversed(tokens):
        if token.isalnum():  
            output.append(token)
        elif token == ')':
            stack.append(token)
        elif token == '(':
            while stack and stack[-1] != ')':
                output.append(stack.pop())
            stack.pop()
        else:  
            while (stack and stack[-1] != ')' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output[::-1]
def tokenize(expression):
    import re
    return re.findall(r'[()]|[a-zA-Z_]\w*|[+\-*/=]', expression)


infix = "F = (m * a) + b"
prefix = infix_to_prefix(infix)
print("Prefix:", prefix)

graph = EquationGraph(prefix)
graph.build_graph()
print("Graph Representation:")
graph.display_graph(graph.root)
