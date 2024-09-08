# Task 1
def SearchA(Arr, x):
    indices = []
    for i in range(len(Arr)):
        if Arr[i] == x:
            indices.append(i)
    return indices
Arr = [22,2,1,7,11,13,5,2,9]
x = int(input("Enter the number: "))
indices =  SearchA(Arr, x)
if indices:
    print ("Index: " , end = "")
    for i in range(len(indices)):
        if i == len(indices) - 1:
            print(indices[i])
        else:
            print(indices[i] , end =",")
else:
    print("Number Not found.")

###################################################################################

# Task 2
def SearchB(Arr, x):
    indices = []
    for i in range(len(Arr)):
        if Arr[i] == x:
            indices.append(i)
        elif Arr[i] > x:
            break
    return indices
Arr = [22,2,1,7,11,13,5,2,9]
Arr.sort()
x = int(input("Enter the number: "))
indices =  SearchB(Arr, x)
if indices:
    print ("Index: " , end = "")
    for i in range(len(indices)):
        if i == len(indices) - 1:
            print(indices[i])
        else:
            print(indices[i] , end =",")
else:
    print("Number Not found.")

###################################################################################

# Task 3
def Minimum(Arr, starting, ending):
    min_index = starting
    for i in range(starting, ending + 1):
        if Arr[i] < Arr[min_index]:
            min_index = i
    return min_index
Arr = [3,4,7,8,0,1,23,-2,-5]
starting = int(input("Starting Index: "))
ending = int(input("Ending Index: "))
index_of_min = Minimum(Arr, starting, ending)
print(f"Index of minimum element: {index_of_min}")

