import numpy as np

# 1. Function to print a 2D matrix
def printMatrix(A, starting_index, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(A[starting_index[0] + i][starting_index[1] + j], end=' ')
        print()  # New line after each row

# 2. Function to add two matrices
def MatAdd(A, B):
    rows = len(A)
    columns = len(A[0])
    result = [[0 for _ in range(columns)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

# 3. Function to add partition of two matrices
def MatAddPartial(A, B, start, size):
    result = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            result[i][j] = A[start[0] + i][start[1] + j] + B[start[0] + i][start[1] + j]
    
    return result

# 4. Iterative function to multiply two matrices
def MatMul(A, B):
    rows_A, columns_A = len(A), len(A[0])
    rows_B, columns_B = len(B), len(B[0])
    
    if columns_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")
    
    result = [[0 for _ in range(columns_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(columns_B):
            for k in range(columns_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# 5. Recursive function to multiply two matrices
def MatMulRecursive(A, B):
    def recursive_mul(A, B, result, i, j, k, n):
        if i < len(A):
            if j < len(B[0]):
                if k < len(A[0]):
                    result[i][j] += A[i][k] * B[k][j]
                    recursive_mul(A, B, result, i, j, k + 1, n)
                else:
                    recursive_mul(A, B, result, i, j + 1, 0, n)
            else:
                recursive_mul(A, B, result, i + 1, 0, 0, n)

    rows_A, columns_B = len(A), len(B[0])
    result = [[0 for _ in range(columns_B)] for _ in range(rows_A)]
    recursive_mul(A, B, result, 0, 0, 0, columns_B)
    
    return result

# 6. Strassen Method for matrix multiplication
def MatMulStrassen(A, B):
    def split(matrix):
        n = len(matrix)
        mid = n // 2
        return (np.array(matrix[:mid, :mid]), np.array(matrix[:mid, mid:]),
                np.array(matrix[mid:, :mid]), np.array(matrix[mid:, mid:]))

    def add(X, Y):
        return X + Y

    def subtract(X, Y):
        return X - Y

    if len(A) == 1:
        return A * B
    
    A11, A12, A21, A22 = split(np.array(A))
    B11, B12, B21, B22 = split(np.array(B))
    
    M1 = MatMulStrassen(add(A11, A22), add(B11, B22))  # (A11 + A22)(B11 + B22)
    M2 = MatMulStrassen(add(A21, A22), B11)             # (A21 + A22)B11
    M3 = MatMulStrassen(A11, subtract(B12, B22))        # A11(B12 - B22)
    M4 = MatMulStrassen(A22, subtract(B21, B11))        # A22(B21 - B11)
    M5 = MatMulStrassen(add(A11, A12), B22)             # (A11 + A12)B22
    M6 = MatMulStrassen(subtract(A21, A11), add(B11, B12))  # (A21 - A11)(B11 + B12)
    M7 = MatMulStrassen(subtract(A12, A22), add(B21, B22))  # (A12 - A22)(B21 + B22)

    C11 = add(subtract(add(M1, M4), M5), M7)  # C11 = M1 + M4 - M5 + M7
    C12 = add(M3, M5)                          # C12 = M3 + M5
    C21 = add(M2, M4)                          # C21 = M2 + M4
    C22 = add(subtract(add(M1, M3), M2), M6)  # C22 = M1 + M3 - M2 + M6

    # Combine the four quadrants into a single result matrix
    new_matrix = np.zeros((len(A), len(B[0])))
    new_matrix[:len(A11), :len(B11[0])] = C11
    new_matrix[:len(A12), len(B11[0]):] = C12
    new_matrix[len(A11):, :len(B21[0])] = C21
    new_matrix[len(A22):, len(B21[0]):] = C22
    
    return new_matrix.tolist()

# Example Usage
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Print Matrix A starting from index (0,0)
print("Matrix A:")
printMatrix(A, (0, 0), len(A), len(A[0]))

# Matrix Addition
print("\nMatrix Addition (A + B):")
result_add = MatAdd(A, B)
printMatrix(result_add, (0, 0), len(result_add), len(result_add[0]))

# Matrix Partial Addition
print("\nPartial Matrix Addition (A and B starting at (1, 1) of size 2):")
result_partial_add = MatAddPartial(A, B, (1, 1), 2)
printMatrix(result_partial_add, (0, 0), len(result_partial_add), len(result_partial_add[0]))

# Matrix Multiplication (Iterative)
print("\nMatrix Multiplication (A * B):")
result_mul = MatMul(A, B)
printMatrix(result_mul, (0, 0), len(result_mul), len(result_mul[0]))

# Matrix Multiplication (Recursive)
print("\nMatrix Multiplication Recursive (A * B):")
result_mul_recursive = MatMulRecursive(A, B)
printMatrix(result_mul_recursive, (0, 0), len(result_mul_recursive), len(result_mul_recursive[0]))

# Strassen Method
print("\nMatrix Multiplication using Strassen (A * B):")
result_strassen = MatMulStrassen(A, B)
printMatrix(result_strassen, (0, 0), len(result_strassen), len(result_strassen[0]))
