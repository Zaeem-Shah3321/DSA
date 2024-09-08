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

