import random

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

class Game:
    def number_game(node, target, max_attempts):
        if not node:
            print("Something went wrong.")
            return

        attempts = 0  
        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess the Computer's number: "))
            
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            attempts += 1 
            if guess == target:
                print(f"\033[34mCorrect! The number was {target}. You guessed it in {attempts} attempts!\033[0m")
                return
            
            elif guess < target:
                print("\033[92mHigher!\033[0m") 
                node = node.right
            
            elif guess > target:
                print("\033[93mLower!\033[0m")  
                node = node.left

        print(f"\033[91mYou lose! The correct number was {target}.\033[0m")

if __name__ == "__main__":
    max_attempts = 6 
    root = build_tree(1, 100)
    target_number = random.randint(1, 100)    
    Game.number_game(root, target_number, max_attempts)