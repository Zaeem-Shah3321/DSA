class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node     

    def delete(self, key):
        current = self.head
        prev = None


        if current and current.data == key:
            self.head = current.next
            current = None
            return


        while current and current.data != key:
            prev = current
            current = current.next


        if not current:
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)

    print("Linked List:")
    ll.display()

    print("Searching for 2:", ll.search(2))
    print("Searching for 4:", ll.search(4))

    print("Deleting 2...")
    ll.delete(2)
    print("Linked List after deletion:")
    ll.display()
