from math import ceil, log

def computeP(A, B):
    P1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
    P2 = (A[1][0] + A[1][1]) * B[0][0]
    P3 = A[0][0] * (B[0][1] - B[1][1])
    P4 = A[1][1] * (B[1][0] - B[0][0])
    P5 = (A[0][0] + A[0][1]) * B[1][1]
    P6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1])
    P7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])

    C12 = P3 + P5
    C21 = P2 + P4
    C11 = P1 + P4 - P5 + P7
    C22 = P1 + P3 - P2 + P6

    C = [[C11, C12],
         [C21, C22]]

    return C


def normalizeMatrix(matrix, upper_bound):
    size = len(matrix)
    for i in range(0, len(matrix)):
        matrix[i].append(0)
    for i in range(size, upper_bound):
        matrix.append(list(0 for j in range(0, upper_bound)))
    return matrix


def strassen(A, B):
    size = len(A)
    C = []

    nextPowerOfTwo = lambda n: 2 ** int(ceil(log(n, 2)))

    if size < nextPowerOfTwo(size):
        A = normalizeMatrix(A, nextPowerOfTwo(size))
        B = normalizeMatrix(B, nextPowerOfTwo(size))

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
    return C


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

print(strassen(matrix, matrix2))
