class ExpressionParser:
    def __init__(self, expression):
        self.expression = expression
        self.operators = set(['+', '-', '*', '/', '(', ')'])
        self.priority = {'+':1, '-':1, '*':2, '/':2}
    def infix_to_prefix(self):
        def precedence(op):
            return self.priority[op] if op in self.priority else 0
        def infix_to_postfix(expression):
            stack = []
            output = []
            for char in expression:
                if char not in self.operators:
                    output.append(char)
                elif char == '(':
                    stack.append('(')
                elif char == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()
                else:
                    while stack and precedence(char) <= precedence(stack[-1]):
                        output.append(stack.pop())
                    stack.append(char)
            while stack:
                output.append(stack.pop())
            return output
        def postfix_to_prefix(postfix):
            stack = []
            for char in postfix:
                if char not in self.operators:
                    stack.append(char)
                else:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(char + op2 + op1)
            return stack[0]
        postfix = infix_to_postfix(self.expression)
        prefix = postfix_to_prefix(postfix)
        return prefix
    def generate_ast(self, prefix):
        class Node:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        stack = []
        for char in reversed(prefix):
            node = Node(char)
            if char in self.operators:
                node.left = stack.pop()
                node.right = stack.pop()
            stack.append(node)
        return stack[-1]
    def print_ast(self, node, level=0):
        if node:
            self.print_ast(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_ast(node.left, level + 1)
if __name__ == "__main__":
    expression = "a+b*c-d/e"
    parser = ExpressionParser(expression)
    prefix = parser.infix_to_prefix()
    print("Prefix:", prefix)
    ast_root = parser.generate_ast(prefix)
    print("Abstract Syntax Tree:")
    parser.print_ast(ast_root)