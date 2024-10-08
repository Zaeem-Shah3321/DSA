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

###################################################################################

# Task 4
def Minimum(Arr, starting, ending):
    min_index = starting
    for i in range(starting, ending + 1):
        if Arr[i] < Arr[min_index]:
            min_index = i
    return min_index
def Sort4(Arr):
    for i in range(len(Arr)):
        min_index = Minimum(Arr, i, len(Arr) - 1)
        Arr[i], Arr[min_index] = Arr[min_index], Arr[i]    
    return Arr
Arr = [3, 4, 7, 8, 0, 1, 23, -2, -5]
sorted_Arr = Sort4(Arr)
print(sorted_Arr)

###################################################################################

# Task 5
def StringReverse(s, starting, ending):
    substring = s[starting:ending]
    return substring[::-1]
starting_index = 27
ending_index = 40  
s = "University of Engineering and Technology Lahore"
reversed_substring = StringReverse(s, starting_index, ending_index)
print(reversed_substring)

###################################################################################

# Task 6
def SumIterative(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total
def SumRecursive(number):
    if number == 0:
        return 0
    return number % 10 + SumRecursive(number // 10)
number = int(input("Enter a number: "))
if number == 0:
    recursive_sum = 0
else:
    recursive_sum = SumRecursive(number)
print(f"Sum of digits is: {recursive_sum}")

###################################################################################

# Task 7
def RowWiseSum(matrix):
    return [sum(row) for row in matrix]
def ColumnWiseSum(matrix):
    num_columns = len(matrix[0])
    column_sums = [0] * num_columns
    for row in matrix:
        for i in range(num_columns):
            column_sums[i] += row[i]
    return column_sums
A = [[1, 13, 13],
    [5, 11, 6],
    [4, 4, 9]]
row_sums = RowWiseSum(A)
print("Row-wise:")
for sum in row_sums:
    print(sum) 
col_sums = ColumnWiseSum(A)
print("Column-wise:", end=" ")
for sum in col_sums:
    print(sum, end=" ")  
print()

###################################################################################

# Task 8
def SortedMerge(arr1, arr2):
    merged = []
    i = 0
    j = 0
    while (i < len(arr1) or j < len(arr2)):
        if (i < len(arr1) and (j == len(arr2) or arr1[i] < arr2[j])):
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    return merged
A = [0, 3, 4, 10, 11]
B = [1, 8, 13, 24]
result = SortedMerge(A, B)
print(result)

###################################################################################

# Task 9
def PalindromRecursive(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return PalindromRecursive(str[1:-1])
input_string = input("Write A Word: ")
if PalindromRecursive(input_string):
    print("Palindrom")
else:
    print("Not Palindrom")

###################################################################################

# Task 10
def sort10(arr):
    negative_numbers = [x for x in arr if x < 0]
    positive_numbers = [x for x in arr if x >= 0]
    negative_numbers.sort()
    positive_numbers.sort()
    result = []
    n_index = 0
    p_indx = 0
    while n_index < len(negative_numbers) and p_indx < len(positive_numbers):
        result.append(negative_numbers[n_index])
        result.append(positive_numbers[p_indx])
        n_index += 1
        p_indx += 1
    while p_indx < len(positive_numbers):
        result.append(positive_numbers[p_indx])
        p_indx += 1
    while n_index < len(negative_numbers):
        result.append(negative_numbers[n_index])
        n_index += 1
    return result
input_array = [10, -1, 9, 20, -3, -8, 22, 9, 7]
output_array = sort10(input_array)
print(output_array)