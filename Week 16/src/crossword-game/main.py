from puzzle import Puzzle

def load_word_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    word_list = load_word_list('../../data/word_list.txt')
    puzzle = Puzzle(10, word_list)
    puzzle.generate()
    puzzle.display()

if __name__ == "__main__":
    main()