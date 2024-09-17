import funcs
import time

def InsertionSort(array, start, end):
    for i in range(start + 1, end + 1):
        key = array[i]
        j = i - 1
        while j >= start and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
def Merge(array, p, q, r):
    num1 = q - p + 1
    num2 = r - q
    L = [0] * num1
    R = [0] * num2
    for i in range(0, num1):
        L[i] = array[p + i]
    for j in range(0, num2):
        R[j] = array[q + 1 + j]
    i = 0
    j = 0
    k = p
    while i < num1 and j < num2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < num1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < num2:
        array[k] = R[j]
        j += 1
        k += 1
def HybridMergeSort(array, start, end, threshold):
    if end - start + 1 <= threshold:
        InsertionSort(array, start, end)
    else:
        if start < end:
            mid = (start + end) // 2
            HybridMergeSort(array, start, mid, threshold)
            HybridMergeSort(array, mid + 1, end, threshold)
            Merge(array, start, mid, end)



def main():
    size = 30000
    threshold = 10
    start = 0
    end = size
    rarray = funcs.RandomArray(size)
    start_time = time.time()
    HybridMergeSort(rarray, start, end - 1, threshold)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Size: {size}, Runtime: {runtime} seconds")
    funcs.sorted_array("HybridMergeSort.csv" , rarray)

if __name__ == "__main__":
    main()

