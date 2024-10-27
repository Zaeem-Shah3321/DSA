class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:
    def __init__(self):
        self.head = Node("head") 
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head.next 
        self.head.next = node 
        self.size += 1

    def pop(self):
        remove = self.head.next
        self.head.next = remove.next 
        self.size -= 1
        return remove.value
    
    def display(self):
        cr = self.head
        val = []
        while cr:
            val.append(str(cr.value))
            cr = cr.next
        return " ".join(val) 




s = stack()
s.push(1)
s.push(2)
s.push(3)

s.pop()
print(s.display())

