def computeP(A, B):
    P1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
    P2 = (A[1][0] + A[1][0]) * B[0][0]
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


def normalizeMatrix(matrix=list()):
    size = matrix.count()
    upper_bound = 1
    while upper_bound < size / 2:
        upper_bound *= 2

    for i in range(size, upper_bound):
        matrix.append(0)

# test commit