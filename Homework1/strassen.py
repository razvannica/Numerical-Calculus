from math import ceil, log

from pip._vendor.requests.packages.urllib3.connectionpool import xrange


def divide(A, B):
    C = [[A[0][0] - B[0][0]] + [A[0][1] - B[0][1]], [A[1][0] - B[1][0]] + [A[1][1] - B[1][1]]]
    return C


def add(A, B):
    C = [[A[0][0] + B[0][0]] + [A[0][1] + B[0][1]]]
    C.append([A[1][0] + B[1][0], A[1][1] + B[1][1]])
    return C


def multiply(A, B):
    C = [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1]
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1]
        ]
    ]
    return C


def computeP(A, B):
    new_size = int(len(A) / 2)
    a11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    a12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    a21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    a22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

    b11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    b12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    b21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
    b22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

    for i in range(0, new_size):
        for j in range(0, new_size):
            a11[i][j] = A[i][j]  # top left
            a12[i][j] = A[i][j + new_size]  # top right
            a21[i][j] = A[i + new_size][j]  # bottom left
            a22[i][j] = A[i + new_size][j + new_size]  # bottom right

            b11[i][j] = B[i][j]  # top left
            b12[i][j] = B[i][j + new_size]  # top right
            b21[i][j] = B[i + new_size][j]  # bottom left
            b22[i][j] = B[i + new_size][j + new_size]  # bottom right

    P1 = multiply(add(a11, a22), add(b11, b22))
    P2 = multiply(add(a21, a22), b11)
    P3 = multiply(a11, divide(b12, b22))
    P4 = multiply(a22, divide(b21, b11))
    P5 = multiply(add(a11, a12), b22)
    P6 = multiply(divide(a21, a11), add(b11, b12))
    P7 = multiply(divide(a12, a22), add(b21, b22))

    C12 = add(P3, P5)
    C21 = add(P2, P4)
    C11 = divide(add(P1, P4), add(P5, P7))
    C22 = divide(add(P1, P3), add(P2, P6))

    return [C11, C12,
            C21, C22]


def normalizeMatrix(matrix, upper_bound):
    size = len(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, upper_bound - len(matrix)):
            matrix[i].append(0)
    for i in range(size, upper_bound):
        matrix.append(list(0 for j in range(0, upper_bound)))
    return matrix


def checkIfPowerOfTwo(no):
    if float(no / 2) > 1.0:
        checkIfPowerOfTwo(no / 2)
    if no == 1.0:
        return 1
    return 0


def strassen_recursive(A, B):
    if len(A) > 4 and len(B) > 4:
        # initializing the new sub-matrices
        new_size = int(len(A) / 2)
        a11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        b11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        for i in range(0, new_size):
            for j in range(0, new_size):
                a11[i][j] = A[i][j]  # top left
                a12[i][j] = A[i][j + new_size]  # top right
                a21[i][j] = A[i + new_size][j]  # bottom left
                a22[i][j] = A[i + new_size][j + new_size]  # bottom right

                b11[i][j] = B[i][j]  # top left
                b12[i][j] = B[i][j + new_size]  # top right
                b21[i][j] = B[i + new_size][j]  # bottom left
                b22[i][j] = B[i + new_size][j + new_size]  # bottom right

        strassen_recursive(a11, b11)
        strassen_recursive(a12, b12)
        strassen_recursive(a21, b21)
        strassen_recursive(a22, b22)

    # TODO : construct C

    C = (computeP(A, B))
    """
    line1 = 0
    line2 = 1

    while line2 < len(A):
        auxC = []
        for i in range(0, len(A) - 1, 2):
            auxC = computeP([
                [A[line1][i], A[line1][i + 1]],
                [A[line2][i], A[line2][i + 1]]
            ],
                [
                    [B[line1][i], B[line1][i + 1]],
                    [B[line2][i], B[line2][i + 1]]
                ]
            )
            if i == 0:
                C.append(auxC[0])
                C.append(auxC[1])
            else:
                C[line1] += auxC[0]
                C[line2] += auxC[1]

        line1 += 2
        line2 += 2
    """
    return C


def strassen(A, B):
    size = len(A)

    if checkIfPowerOfTwo(size) != 1:
        nextPowerOfTwo = lambda n: 2 ** int(ceil(log(n, 2)))
        if size < nextPowerOfTwo(size):
            A = normalizeMatrix(A, nextPowerOfTwo(size))
            B = normalizeMatrix(B, nextPowerOfTwo(size))

    return strassen_recursive(A, B)


matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
matrix2 = [[0, 1, 2, 3, 4],
           [0, 1, 2, 3, 4],
           [0, 1, 2, 3, 4],
           [0, 1, 2, 3, 4],
           [0, 1, 2, 3, 4]]

result = strassen(matrix, matrix2)
for i in range(0, len(result)):
    print(result[i])


def ikj_matrix_product(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

"""
result2 = ikj_matrix_product(matrix, matrix2)
for i in range(0, len(result2)):
    print(result2[i])
"""