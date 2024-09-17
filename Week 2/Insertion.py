import time
import funcs
def InsertionSort(array,start,end):
    for i in range(start,end):
        key  = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key    
    return array

def main():
    size = 30000
    start = 0
    end = size
    rarray = funcs.RandomArray(size)
    start_time = time.time()
    r = InsertionSort(rarray, start, end)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Size: {size}, Runtime: {runtime} seconds")
    funcs.sorted_array("InsertionSort.csv" , r)

if __name__ == "__main__":
    main()

