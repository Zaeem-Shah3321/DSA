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

class StackUsingQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        self.queue1.enqueue(value)

    def pop(self):
        if self.queue1.is_empty():
            raise Exception("Stack is empty")

        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        popped_value = self.queue1.dequeue()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_value

    def is_empty(self):
        return self.queue1.is_empty()

    def display(self):
        if self.queue1.is_empty():
            return "Stack is empty"

        values = []
        while not self.queue1.is_empty():
            value = self.queue1.dequeue()
            values.append(str(value))
            self.queue2.enqueue(value)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return " -> ".join(reversed(values))
