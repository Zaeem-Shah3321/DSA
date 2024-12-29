class TreeNode:
    def __init__(self, key, obj):
        self.key = key
        self.obj = obj
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, obj):
        if not self.root:
            self.root = TreeNode(key, obj)
        else:
            self._insert(self.root, key, obj)

    def _insert(self, node, key, obj):

        if key < node.key: 
            if node.left:
                self._insert(node.left, key, obj)
           
            else:
                node.left = TreeNode(key, obj)

        elif key > node.key:
            if node.right:
                self._insert(node.right, key, obj)
           
            else:
                node.right = TreeNode(key, obj)
        else:
            print(f"Key '{key}' already exists. Skipping insertion.")

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        
        if key == node.key:
            return node.obj
    
        elif key < node.key:
            return self._search(node.left, key)
    
        else:
            return self._search(node.right, key)