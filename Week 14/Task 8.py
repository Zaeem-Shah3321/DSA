def evaluate_rpn(expression):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b) 
    return stack[0]
if __name__ == "__main__":
    expression = input("Enter RPN expression: ")
    result = evaluate_rpn(expression)
    print("Output:", result)