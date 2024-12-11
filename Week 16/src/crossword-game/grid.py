class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(' '.join(row))

    def place_word(self, word, row, col, direction):
        if direction == 'H':
            for i in range(len(word)):
                self.grid[row][col + i] = word[i]
        elif direction == 'V':
            for i in range(len(word)):
                self.grid[row + i][col] = word[i]

    def can_place_word(self, word, row, col, direction):
        if direction == 'H':
            if col + len(word) > self.size:
                return False
            for i in range(len(word)):
                if self.grid[row][col + i] not in (' ', word[i]):
                    return False
        elif direction == 'V':
            if row + len(word) > self.size:
                return False
            for i in range(len(word)):
                if self.grid[row + i][col] not in (' ', word[i]):
                    return False
        return True