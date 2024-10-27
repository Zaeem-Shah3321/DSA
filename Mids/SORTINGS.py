def bubble2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr


def selection2(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1 , n):
            if arr[j] < arr[min]:
                min = j
        arr[i] , arr[min] = arr[min] , arr[i]
    return arr    


def insertion2(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key 
    return arr


def merge2(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        l = merge2(arr[:mid])
        r = merge2(arr[mid:])
        return merge2S(l,r)
    else:
        return arr 

def merge2S(left,right):
    sorted = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    sorted.extend(left[i:])            
    sorted.extend(right[j:])            
    return sorted

def bucket2(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        bi = int(n*num)
        buckets[bi].append(num)
    for buck in buckets:
        buck = insertion2(buck)
    index = 0
    for buck in buckets:
        for num in buck:
            arr[index] = num
            index += 1
    return arr        

def count2 (arr):
    n = len(arr)
    maxl = max(arr)
    count = [0] * (maxl + 1)
    out = [0] * (n)

    for i in range(n):
        count[arr[i]] += 1
        
    for j in range (1 , len(count)):
        count[j] += count[j-1]

    for k in range(n):
        value = arr[k]
        count[value] -= 1
        out[count[value]] = value
    return out

def quick2(arr,low,high):
    if low < high:
        piv = part2(arr,low,high)
        quick2(arr,low, piv - 1)
        quick2(arr,piv + 1, high)
    return arr

def part2(arr,lo,hi):
    pi = arr[hi]
    i = lo - 1
    for j in range(lo,hi):
        if arr[j] < pi:
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[hi] = arr[hi] , arr[i+1]
    return i+1
 
def radix(arr):
    maxl = max(arr)
    exp = 1
    while maxl / exp >= 1:
        arr = countRad(arr,exp)
        exp *= 10
    return arr 
 
def countRad(arr,exp):
    n = len(arr)
    count = [0] * (10)
    out  = [0] * (n)

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range (1,10):
        count [i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        out[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    return out


array = [64, 34, 25, 12, 22, 11, 90]
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

print (insertion2(arr))