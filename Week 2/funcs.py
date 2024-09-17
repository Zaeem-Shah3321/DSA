import random
import csv
import time

def RandomArray(size):
    arr = []
    for i in range(size):
        rand = random.randint(-15000,15000)
        arr.append(rand)
    return arr

def sorted_array(file_name, sorted_array):
    with open(file_name, 'w', newline='\n') as f:
        writer = csv.writer(f)
        for el in sorted_array:
            writer.writerow([el])

def calculate_time(func, *args):
    start_time = time.perf_counter()
    ans = func(*args)
    end_time = time.perf_counter()
    runtime = end_time - start_time
    return ans, runtime


if __name__=="__main__":
    size = int(input("Enter Array Size: "))
    rarray = RandomArray(size)
    print(rarray)
