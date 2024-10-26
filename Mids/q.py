class Queue:
    def __init__(self):
        self.Q = [None] * 10
        self.rear = -1
    
    def size(self):
        return self.rear+1

    def resize(self):
        newQ = [None] * (len(self.Q) * 2)
        if self.rear >= len(self.Q):
            for i in range(self.size()):
                newQ[i] = self.Q[i]
            self.Q = newQ

    def enqueue(self, item):
        if self.rear+1 >= len(self.Q):
            self.resize()
        
        self.rear+=1
        self.Q[self.rear] = item
    
    def dequeue(self):
        if self.rear==-1: return

        value = self.Q[0]
        for i in range(self.size()-1):
            self.Q[i] = self.Q[i+1]
        self.rear-=1
        return value
        
    def display(self):
        for i in range(self.size()):
            print(f"Element at {i} = {self.Q[i]}")
