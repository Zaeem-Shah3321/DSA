import funcs
import time

def MergeSort(array, start, end):
    if end - start <= 1:
        return
    mid = (start + end) // 2 
    MergeSort(array, start, mid)
    MergeSort(array, mid, end)    
    Merge(array, start, mid, end)

def Merge(array, p, q, r):
    left = array[p:q]
    right = array[q:r]
    i = j = 0
    k = p
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

def main():
    size = 30000
    start = 0
    end = size
    rarray = funcs.RandomArray(size)
    start_time = time.time()
    MergeSort(rarray, start, end)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Size: {size}, Runtime: {runtime} seconds")
    funcs.sorted_array("MergeSort.csv" , rarray)

if __name__ == "__main__":
    main()
