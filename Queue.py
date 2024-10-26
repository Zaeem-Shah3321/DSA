class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        values = []
        current = self.front
        while current:
            values.append(str(current.value))
            current = current.next
        if values:
            return " ".join(values)
        else:
            return "Queue Is Empty"
        
    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        remove = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return remove.value

    def display(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.front.value
