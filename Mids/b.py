class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rare = None
        self.size = 0

    def enqueue(self,value):
        node = Node(value)
        if self.rare:
            self.rare.next = node
        self.rare = node
        if not self.front:
            self.front = node
        self.size += 1

    def dequeue(self):
        remove = self.front
        self.front = self.front.next
        if not self.front:
            self.rare = None
        self.size -= 1
        return remove.value

    def dispaly(self):
        value = []
        cr = self.front
        while cr:
            value.append(str(cr.value))
            cr = cr.next
        return " ".join(value)
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dispaly())