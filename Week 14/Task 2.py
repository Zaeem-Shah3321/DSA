class FinancialCalculator:
    def __init__(self):
        self.operators = set(['+', '-', '*', '/', '(', ')'])
        self.priority = {'+':1, '-':1, '*':2, '/':2}
    def infix_to_postfix(self, expression):
        stack = [] 
        output = ''
        for ch in expression:
            if ch not in self.operators: 
                output+= ch
            elif ch=='(': 
                stack.append('(')
            elif ch==')':
                while stack and stack[-1]!= '(':
                    output+=stack.pop()
                stack.pop()
            else:
                while stack and stack[-1]!='(' and self.priority[ch]<=self.priority[stack[-1]]:
                    output+=stack.pop()
                stack.append(ch)
        while stack:
            output+=stack.pop()
        return output
    def evaluate_postfix(self, expression):
        stack = []
        for ch in expression:
            if ch not in self.operators:
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
                elif ch == '/':
                    stack.append(a / b)
        return stack[0]
    def calculate(self, expression):
        postfix = self.infix_to_postfix(expression)
        return self.evaluate_postfix(postfix)
if __name__ == "__main__":
    calc = FinancialCalculator()
    expression = input("Enter an arithmetic expression: ")
    result = calc.calculate(expression)
    print(f"The result is: {result}")