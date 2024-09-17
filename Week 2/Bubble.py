import funcs
import time

def BubbleSort(arrr, start, end):
    for i in range(start, end - 1):
        for j in range(start, end - i - 1):
            if arrr[j] > arrr[j + 1]:
                arrr[j], arrr[j + 1] = arrr[j + 1], arrr[j]
    return arrr


def main():
    size = 30000
    start = 0
    end = size
    rarray = funcs.RandomArray(size)
    start_time = time.time()
    r = BubbleSort(rarray, start, end)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Size: {size}, Runtime: {runtime} seconds")
    funcs.sorted_array("BubbleSort.csv" , r)

if __name__ == "__main__":
    main()
