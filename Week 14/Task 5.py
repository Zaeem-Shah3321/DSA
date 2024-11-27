class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class ExpressionParser:
    def __init__(self):
        self.operators = set(['+', '-', '*', '/', '^'])
    def is_operator(self, c):
        return c in self.operators
    def construct_tree(self, expression):
        stack = []
        expression = expression.split()
        for token in reversed(expression):
            if not self.is_operator(token):
                node = Node(token)
                stack.append(node)
            else:
                node = Node(token)
                node.left = stack.pop()
                node.right = stack.pop()
                stack.append(node)
        return stack[-1]
    def print_prefix(self, node):
        if node:
            print(node.value, end=' ')
            self.print_prefix(node.left)
            self.print_prefix(node.right)
    def convert_to_prefix(self, expression):
        root = self.construct_tree(expression)
        self.print_prefix(root)
        print()
if __name__ == "__main__":
    parser = ExpressionParser()
    expression = "a + b"
    print("Prefix notation:")
    parser.convert_to_prefix(expression)