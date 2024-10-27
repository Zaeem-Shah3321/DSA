class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rare = None
        self.size = 0

    def isEmpty(self):
        return self.front is None

    def enqueue(self,value):
        node = Node(value)
        if self.rare:
            self.rare.next = node
        self.rare = node
        if not self.front:
            self.front = node
        self.size +=1

    def dequeue(self):
        if self.isEmpty():
            raise Exception ("Queue Is Empty")
        remove =  self.front
        self.front = self.front.next
        if not self.front:
            self.rare = None
        self.size -= 1
        return remove.value

    def dispaly(self):
        if self.isEmpty():
            raise Exception("Queue Is Empty")
        current = self.front
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return " ".join(values)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dispaly())