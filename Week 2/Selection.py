import funcs
import time

def SelectionSort(arrr,start,end):
    for i in range(start,end-1):
        min = i
        for j in range(i+1,end):
            if arrr[j] < arrr[min]:
                min = j
        arrr[i],arrr[min] = arrr[min],arrr[i]
    return arrr

def main():
    size = 300
    start = 0
    end = size
    rarray = funcs.RandomArray(size)
    start_time = time.time()
    r = SelectionSort(rarray, start, end)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Size: {size}, Runtime: {runtime} seconds")
    funcs.sorted_array("SelectionSort.csv" , r)

if __name__ == "__main__":
    main()
