from grid import Grid
from trie import Trie
import random

class Puzzle:
    def __init__(self, size, word_list):
        self.grid = Grid(size)
        self.trie = Trie()
        for word in word_list:
            self.trie.insert(word)

    def generate(self):
        words = list(self.trie.root.children.keys())
        random.shuffle(words)
        for word in words:
            placed = False
            for _ in range(100):  
                row = random.randint(0, self.grid.size - 1)
                col = random.randint(0, self.grid.size - 1)
                direction = random.choice(['H', 'V'])
                if self.grid.can_place_word(word, row, col, direction):
                    self.grid.place_word(word, row, col, direction)
                    placed = True
                    break
            if not placed:
                print(f"Could not place word: {word}")

    def display(self):
        self.grid.display()