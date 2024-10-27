# Algorith Number 1
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr    

# Algorith Number 2
def selection(arr):
    n = len(arr)
    for i in range (n):
        min = i
        for j in range (i+1 ,n):
            if arr[j] < arr[min]:
                min = j
        arr[i] , arr[min] = arr[min] , arr[i]
    return arr

# Algorith Number 3
def insertion(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i -1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr    

# Algorith Number 4
def quick(arr,l,h):
    if l < h:
        p = part(arr,l,h)
        quick(arr,l,p-1)
        quick(arr,p+1,h)
    return arr

def part(arr,lo,hi):
    piv = arr[hi]
    i = lo - 1
    for j in range(lo,hi):
        if arr[j] < piv:
            i+=1
            arr[i] ,arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[hi] = arr[hi] , arr[i+1]
    return i+1        

# Algorith Number 5
def merge(arr):
    n = len(arr)
    if n > 1:
        mid = n//2

        left = merge(arr[:mid])
        right = merge(arr[mid:])

        a =  mergeS(left,right)
        return a
    else:
        return arr    
    
def mergeS(l,r):
    sorted = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            sorted.append(l[i])
            i+=1
        else:
            sorted.append(r[j])
            j+=1
        
    sorted.extend(l[i:])
    sorted.extend(r[j:])
    return sorted
        
# Algorith Number 6
def count(arr):
    n = len(arr)
    maxl = max(arr)
    count = [0] * (maxl + 1)
    out = [0] * (n)

    for i in range(n) :
        count[arr[i]] += 1

    for i in range (1,len(count)):
        count[i] += count[i-1]
           
    for i in range (n):
        value = arr[i]
        count[value] -= 1
        out[count[value]] = value

    return out

# Algorith Number 7
def radix(arr):
    maxl = max(arr)
    exp = 1
    while maxl / exp >= 1:
        arr = countRad(arr,exp)
        exp *= 10
    return arr

def countRad(arr,exp):
    n = len(arr)
    out = [0] * (n)
    count = [0] * (10)

    for i in range (n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range (1,10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        out[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    return out    

# Algorith Number 8
def bucket(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)
    for buck in buckets:
        buck = insertion(buck)
    index = 0
    for bucks in buckets:
        for num in bucks:
            arr[index] = num
            index += 1
    return arr    

# Algorithm Number 9
def gnome(arr):
    index = 0
    n = len(arr)
    while index < n:
        if index == 0 or (arr[index] >= arr[index - 1]):
            index += 1
        else:
            arr[index] , arr[index - 1] = arr[index - 1] , arr[index]
            index -= 1
    return arr        
    









array = [64, 34, 25, 12, 22, 11, 90]
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

print (bubble(array))