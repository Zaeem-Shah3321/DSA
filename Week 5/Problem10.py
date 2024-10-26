import time

def main():
    numbers = []
    append_times = []
    for i in range(1, 101):
        start_time = time.perf_counter()  
        numbers.append(i)                  
        end_time = time.perf_counter()     
  
        time_taken = end_time - start_time
        append_times.append(time_taken)
        
        print(f"Appended {i} in {time_taken:.10f} seconds")
    print(f"Total time taken for appending 1 to 100: {sum(append_times):.10f} seconds")

if __name__ == "__main__":
    main()
