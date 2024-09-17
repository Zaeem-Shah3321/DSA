import funcs
from Insertion import InsertionSort
from MergeSort import MergeSort

with open("word.txt") as f:
    words = f.read().splitlines()

start, end = 0, len(words)

result, runtime = funcs.calculate_time(MergeSort, words, start, end)
print(f"MergeSort before shuffling: {runtime:.20f} seconds")
result, runtime = funcs.calculate_time(InsertionSort, words, start, end)
print(f"InsertionSort before shuffling: {runtime:.20f} seconds")


result, runtime = funcs.calculate_time(MergeSort, words, start, end)
print(f"MergeSort after shuffling: {runtime:.20f} seconds")
result, runtime = funcs.calculate_time(InsertionSort, words, start, end)
print(f"InsertionSort after shuffling: {runtime:.20f} seconds")