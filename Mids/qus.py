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


class QueueUsingStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                raise Exception("Queue is empty")

            while self.stack1:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def display(self):
        if self.is_empty():
            return "Queue is empty"
        values = self.stack2[::-1] + self.stack1
        return " -> ".join(map(str, values))
