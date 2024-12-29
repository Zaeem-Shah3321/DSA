class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  
        self.right = None 

def build_tree(low, high):
    if low > high:
        return None
    
    mid = (low + high) // 2

    root = TreeNode(mid)

    root.left = build_tree(low, mid - 1) 
    root.right = build_tree(mid + 1, high)

    return root

def play_game(node):
    if not node:
        return

    print(f"\033[32mIs your number {node.value}?\033[0m")
    answer = input("((1) Yes (2) Higher (3) Lower) Chose Number: ").lower()

    if answer == "1":
        print("\033[94mYay! I guessed your number!\033[0m")
        return
    
    elif answer == "2":
        if node.right:
            play_game(node.right)
        else:
            print("Something went wrong. Did you choose a valid number?")

    elif answer == "3":
        if node.left:
            play_game(node.left)
        else:
            print("Something went wrong. Did you choose a valid number?")
    
    else:
        print("Invalid input. Please respond with '1', '2', or '3'.")

if __name__ == "__main__":
    print("Think of a number between 1 and 100, and I will try to guess it!")
    root = build_tree(1, 100)
    play_game(root)
