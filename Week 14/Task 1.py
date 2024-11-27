class ExpressionConverter:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def __init__(self, expression):
        self.expression = expression
    @staticmethod
    def is_operator(c):
        return c in ['+', '-', '*', '/', '^']
    @staticmethod
    def is_operand(c):
        return c.isalnum()
    def infix_to_postfix(self):
        stack = []
        postfix = []
        for char in self.expression:
            if self.is_operand(char):
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and self.precedence[char] <= self.precedence.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(char)
        while stack:
            postfix.append(stack.pop())
        return ''.join(postfix)
    def infix_to_prefix(self):
        reversed_expression = self.expression[::-1]
        adjusted_expression = reversed_expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')
        postfix = ExpressionConverter(adjusted_expression).infix_to_postfix()
        return postfix[::-1]
    def postfix_to_infix(self, postfix):
        stack = []
        for char in postfix:
            if self.is_operand(char):
                stack.append(char)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(f'({op2}{char}{op1})')
        return stack[-1]
    def prefix_to_infix(self, prefix):
        stack = []
        for char in reversed(prefix):
            if self.is_operand(char):
                stack.append(char)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(f'({op1}{char}{op2})')
        return stack[-1]
expression = "a+b*(c^d-e)^(f+g*h)-i"
converter = ExpressionConverter(expression)
print("Infix Expression:", expression)
postfix = converter.infix_to_postfix()
print("Postfix Expression:", postfix)
prefix = converter.infix_to_prefix()
print("Prefix Expression:", prefix)
print("Converted back to Infix from Postfix:", converter.postfix_to_infix(postfix))
print("Converted back to Infix from Prefix:", converter.prefix_to_infix(prefix))
