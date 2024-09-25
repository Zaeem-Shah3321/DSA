import time
import csv
import funcs 
from Bubble import BubbleSort
from Selection import SelectionSort
from Insertion import InsertionSort
from MergeSort import MergeSort
from HybridMergeSort import HybridMergeSort

def read_n_values(filename):
    with open(filename, 'r') as file:
        n_values = [int(line.strip()) for line in file]
    return n_values

def write_in_file(filename, row):
    file_exists = False
    try:
        with open(filename, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['n', 'BubbleSortTime(s)' , 'SelectionSortTime(s)' , 'InsertionSortTime(s)', 'MergeSortTime(s)', 'HybridMergeSortTime(s)'])
        writer.writerow(row)

n_values = read_n_values('Nvalues.txt')

for n in n_values:
    array = funcs.RandomArray(n)

    array_copy = array.copy()
    start_time = time.time()
    BubbleSort(array_copy, 0, n - 1)
    bubble_time = time.time() - start_time

    array_copy = array.copy()
    start_time = time.time()
    SelectionSort(array_copy, 0, n - 1)
    selection_time = time.time() - start_time

    array_copy = array.copy()
    start_time = time.time()
    InsertionSort(array_copy, 0, n - 1)
    insertion_time = time.time() - start_time
    
    array_copy = array.copy() 
    start_time = time.time()
    MergeSort(array_copy, 0, n - 1)
    merge_time = time.time() - start_time
    
    array_copy = array.copy()
    start_time = time.time()
    HybridMergeSort(array_copy, 0, n - 1, 10)
    hybrid_merge_time = time.time() - start_time
    
    row = [n, bubble_time, selection_time, insertion_time, merge_time, hybrid_merge_time]
    write_in_file('RunTime.csv', row)
    
    print(f'n = {n}') 
    print(f'BubbleSort Time = {bubble_time}s')
    print(f'SelectionSort Time = {selection_time}s')
    print(f'InsertionSort Time = {insertion_time}s')
    print(f'MergeSort Time = {merge_time}s')
    print(f'HybridMergeSort Time = {hybrid_merge_time}s')
