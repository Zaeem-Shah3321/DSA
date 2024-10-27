class Node:
    def __init__(self,value):
        self.value =  value 
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size  = 0

    def push(self,value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1

    def display(self):
        cr = self.head
        val = []
        while cr:
            val.append(str(cr.value))
            cr = cr.next
        return " " .join(val)
    
s = Stack()
s.push(10)
s.push(20)
s.pop()
print(s.display())