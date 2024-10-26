class Stack:
    def __init__(self):
        self.Stack = [None] * 10
        self.top = -1

    def push(self, item):
        if self.top+1 >= len(self.Stack):
            self.resize()
        self.top+=1
        self.Stack[self.top] = item
            
    def resize(self):
        newStack = [None] * (len(self.Stack)*2)
        for i in range(self.size()):
            newStack[i] = self.Stack[i]
        self.Stack = newStack

    def size(self):
        return self.top+1

    def display(self):
        for i in range(self.size()):
            print(f"Element at {i} = {self.Stack[i]}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        value = self.Stack[self.top]
        self.Stack[self.top] = None
        self.top -= 1
        return value
        
    def is_empty(self):
        if self.top == -1: return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.Stack[self.top]


class Stueue:
    def __init__(self, og):
        self.original = og
        self.left = Stack()
        self.right = Stack()

        self.init()
    
    def init(self):
        mid = self.original.size() // 2
        
        for i in range(mid):
            self.left.push(self.original.pop())
        
        for i in range(self.left.size()):
            self.right.push(self.left.pop())

        for i in range(self.original.size()):
            self.left.push(self.original.pop())
    
    def again(self):
        if self.left.is_empty() or self.right.is_empty():
            self.populateOG()
            self.init()

    def pop(self):
        self.again()
        return self.right.pop()
            
    def push(self, item):
        self.again()
        self.right.push(item)

    def enqueue(self, item):
        self.again()
        self.push(item)
            
    def dequeue(self):
        self.again()
        return self.left.pop()
    
    def populateOG(self):
        for i in range(self.left.size()):
            self.original.push(self.left.pop())
        
        for j in range(self.right.size()):
            self.left.push(self.right.pop())

        for k in range(self.left.size()):
            self.original.push(self.left.pop())

    def display(self):
        self.populateOG()
        self.original.display()
        self.init()

stk = Stack()

stk.push(0)
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

stu = Stueue(stk)

stu.pop()
stu.dequeue()

stu.display()
