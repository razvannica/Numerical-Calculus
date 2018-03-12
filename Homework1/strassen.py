from math import ceil, log

def read_from_file(filename):
    lines = open(filename, 'r').read()
    A = []
    B = []
    data = [item.split() for item in lines.split('\n')[:-1]]

    size = int(data[0][0])
    lower_limit = int(data[1][0])
    data.pop(0)
    data.pop(0)
    i = 0
    j = 0
    ok = 0
    for line in data:
        if i <= 9 and ok == 0:
            if line:
                for index in range(size):
                    if index==0:
                        A.append([])
                    A[i]+=line[index]
                i+= 1
        else:
            ok = 1
            if line:
                for index in range(size):
                    if index==0:
                        B.append([])
                    B[j]+=line[index]
                j+= 1

    for line in range(size):
        for column in range(size):
            A[line][column] = int(A[line][column])
            B[line][column] = int(B[line][column])

    return A, B, size, lower_limit


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
            C[line][column] = int(A[line][column]) + int(B[line][column])
    return C


def computeP(A, B, size, lower_limit):
    n = len(A)
    new_size = int(n / 2)
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

    P1 = strassen_recursive(matrix_add(A11, A22), matrix_add(B11, B22),size, lower_limit)
    P2 = strassen_recursive(matrix_add(A21, A22), B11,size,lower_limit)
    P3 = strassen_recursive(A11, matrix_divide(B12, B22),size,lower_limit)
    P4 = strassen_recursive(A22, matrix_divide(B21, B11),size,lower_limit)
    P5 = strassen_recursive(matrix_add(A11, A12), B22,size,lower_limit)
    P6 = strassen_recursive(matrix_divide(A21, A11), matrix_add(B11, B12),size,lower_limit)
    P7 = strassen_recursive(matrix_divide(A12, A22), matrix_add(B21, B22),size,lower_limit)

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


def strassen_recursive(A, B, size, lower_limit):
    if len(A) <= lower_limit and len(B) <= lower_limit:
        return matrix_multiplication(A, B)
    else:
        return computeP(A, B, size, lower_limit)


def strassen(A, B, size, lower_limit):

    if check_if_power_of_two(size) != 1:
        next_power_of_two = lambda n: 2 ** int(ceil(log(n, 2)))
        if size < next_power_of_two(size):
            A = normalize_matrix(A, next_power_of_two(size))
            B = normalize_matrix(B, next_power_of_two(size))

    auxC = strassen_recursive(A, B, len(A),lower_limit)
    C = [[0 for i in range(size)] for j in range(size)]
    for line in range(size):
        for column in range(size):
            C[line][column] = auxC[line][column]
    return C

A, B, size, lower_limit = read_from_file("matrix_input.in")

result = strassen(A, B, size, lower_limit)
for i in range(0, len(result)):
    print(result[i])
