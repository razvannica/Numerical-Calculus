from math import ceil, log

def normalize_matrix(matrix, upper_bound):
    size = len(matrix)
    for line in range(0, len(matrix)):
        for column in range(0, upper_bound - len(matrix)):
            matrix[line].append(0)
    for line in range(size, upper_bound):
        matrix.append(list(0 for j in range(0, upper_bound)))
    return matrix

def check_if_power_of_two(no):
    if float(no / 2) > 1.0:
        check_if_power_of_two(no / 2)
    if no == 1.0:
        return 1
    return 0

def matrix_multiplication(A, B):
    size = len(A)
    C = [[0 for i in range(size)] for j in range(size)]
    for line in range(size):
        for column in range(size):
            for index in range(size):
                C[line][index] += A[line][column] * B[column][index]
    return C

def matrix_divide(A, B):
    size = len(A)
    C = [[0 for j in range(0, size)] for i in range(0, size)]
    for line in range(0, size):
        for column in range(0, size):
            C[line][column] = A[line][column] - B[line][column]
    return C

def matrix_add(A, B):
    size = len(A)
    C = [[0 for j in range(0, size)] for i in range(0, size)]
    for line in range(0, size):
        for column in range(0, size):
            C[line][column] = A[line][column] + B[line][column]
    return C

def computeP(A, B):
    size = len(A)
    new_size = int(size / 2)
    A11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    A12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    A21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    A22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

    B11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    B12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    B21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    B22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

    for line in range(0, new_size):
        for column in range(0, new_size):
            A11[line][column] = A[line][column]
            A12[line][column] = A[line][column + new_size]
            A21[line][column] = A[line + new_size][column]
            A22[line][column] = A[line + new_size][column + new_size]

            B11[line][column] = B[line][column]
            B12[line][column] = B[line][column + new_size]
            B21[line][column] = B[line + new_size][column]
            B22[line][column] = B[line + new_size][column + new_size]

    P1 = strassen_recursive(matrix_add(A11, A22), matrix_add(B11, B22))
    P2 = strassen_recursive(matrix_add(A21, A22), B11)
    P3 = strassen_recursive(A11, matrix_divide(B12, B22))
    P4 = strassen_recursive(A22, matrix_divide(B21, B11))
    P5 = strassen_recursive(matrix_add(A11, A12), B22)
    P6 = strassen_recursive(matrix_divide(A21, A11), matrix_add(B11, B12))
    P7 = strassen_recursive(matrix_divide(A12, A22), matrix_add(B21, B22))

    C11 = matrix_add(matrix_divide(matrix_add(P1, P4), P5), P7)
    C12 = matrix_add(P3, P5)
    C21 = matrix_add(P2, P4)
    C22 = matrix_add(matrix_divide(matrix_add(P1, P3), P2), P6)

    C = [[0 for j in range(0, size)] for i in range(0, size)]
    for line in range(0, new_size):
        for column in range(0, new_size):
            C[line][column] = C11[line][column]
            C[line][column + new_size] = C12[line][column]
            C[line + new_size][column] = C21[line][column]
            C[line + new_size][column + new_size] = C22[line][column]
    return C

def strassen_recursive(A, B):
    if len(A) == 2 and len(B) == 2:
        return matrix_multiplication(A, B)
    else:
        return computeP(A, B)

def strassen(A, B):
    size = len(A)

    if check_if_power_of_two(size) != 1:
        nextPowerOfTwo = lambda n: 2 ** int(ceil(log(n, 2)))
        if size < nextPowerOfTwo(size):
            A = normalize_matrix(A, nextPowerOfTwo(size))
            B = normalize_matrix(B, nextPowerOfTwo(size))

    auxC = strassen_recursive(A, B)
    C = [[0 for i in range(size)] for j in range(size)]
    for line in range(size):
        for column in range(size):
            C[line][column] = auxC[line][column]
    return C


matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
          ]
matrix2 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

result = strassen(matrix, matrix2)
for i in range(0, len(result)):
    print(result[i])

