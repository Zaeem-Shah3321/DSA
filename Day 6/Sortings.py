def bubble_sort(arr,key):
    n = len(arr)

    for i in range (n-1):
        for j in range(n-1):
            if arr[j][key] > arr[j+1][key]:
                arr[j],arr[j+1] = arr[j+1] , arr[j]
    
    return arr

def selection_sort(arr, key):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j][key] < arr[min_idx][key]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def insertion_sort(arr, key):
    n = len(arr)
    
    for i in range(1, n):
        current = arr[i]
       
        j = i - 1
        while j >= 0 and arr[j][key] > current[key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    
    return arr

def merge_sort(arr, key):
    
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    
    left_half = merge_sort(arr[:mid], key)
    right_half = merge_sort(arr[mid:], key)
    
    return merge(left_half, right_half, key)

def merge(left, right, key):
    sorted_list = []
    
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            sorted_list.append(left[i])
            i += 1
    
        else:
            sorted_list.append(right[j])
            j += 1
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

def quick_sort(arr, low, high, key):
    if low < high:
        pi = partition(arr, low, high, key)
    
        quick_sort(arr, low, pi - 1, key)
        quick_sort(arr, pi + 1, high, key) 
         
def partition(arr, low, high, key):
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j][key] <= pivot[key]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


if __name__ == "__main__":
   
    array = [
        {"name": "Bob Smith", "phone": "9876543210"},
        {"name": "Evan Davis", "phone": "3332221111"},
        {"name": "Charlie Brown", "phone": "5556667777"},
        {"name": "Alice Johnson", "phone": "1234567890"},
        {"name": "Diana Prince", "phone": "4445556666"}
    ]

   
    quick_sort(array,0,len(array)-1,"name")
    for contact in array:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")