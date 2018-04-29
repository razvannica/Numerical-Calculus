"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import copy


def read_file(path, to_check):
    size = 0
    input_list = []
    matrix = []

    with open(path) as file:
        k = 0

        for num, lines in enumerate(file, 1):
            if num < size + 3 and k != 0:
                try:
                    input_list.append(float(lines.split()[0]))
                except:
                    continue

            if k == 0:
                size = int(lines.split()[0])
                k = 1
                matrix = [[] for i in range(0, size)]

            if num > size + 3:
                line = lines.split(",")
                value = float(line[0])
                index_line = int(line[1])
                index_col = int(line[2])

                if index_line == index_col:
                    ok = 0
                    for matrix_line in matrix[index_line]:
                        if len(matrix_line) > 1:
                            if matrix_line[1] == index_col:
                                matrix_line[0] += value
                                ok = 1
                                break
                    if ok == 0:
                        matrix[index_line].append(list((value, index_col)))
                else:
                    ok = 0
                    for matrix_line in matrix[index_line]:
                        if len(matrix_line) > 1:
                            if matrix_line[1] == index_col:
                                matrix_line[0] += value
                                ok = 1
                                break
                    if ok == 0:
                        matrix[index_line].insert(0, list((value, index_col)))

    if to_check:
        for index_line in range(0, size):
            if len(matrix[index_line]) > 10:
                print(matrix[index_line])
                raise ValueError("The matrix has more than 10 inputs into line " + str(index_line))
    return size, input_list, matrix


def matrix_sum(A, B, size):
    C = [[] for i in range(0, size)]

    for C_line_index in range(0, size):
        C[C_line_index] = copy.copy(A[C_line_index])

        for B_line in B[C_line_index]:
            C_index = -1

            for i in range(0, len(C[C_line_index])):
                if C[C_line_index][i][1] == B_line[1]:
                    C_index = i
                    break

            if C_index != -1:
                C[C_line_index][C_index][0] += B_line[0]
            else:
                C[C_line_index].insert(0, B_line)

    for C_line_index in range(0, size):
        if len(C[C_line_index]) > 20:
            raise ValueError("More than 20 null elements on line: " + str(C_line_index))
    return C


def matrix_product(A, B, n):
    C = [[] for i in range(0, n)]
    for C_line_index in range(0, n):
        for A_line in A[C_line_index]:
            for B_element in B[A_line[1]]:
                C_index = -1

                for i in range(0, len(C[C_line_index])):
                    if C[C_line_index][i][1] == B_element[1]:
                        C_index = i
                        break

                if C_index != -1:
                    product = B_element[0] * A_line[0]
                    C[C_line_index][C_index][0] += product
                else:
                    C[C_line_index].insert(0, list((B_element[0] * A_line[0], B_element[1])))
    return C


"""
    Result checking methods
"""


def matrix_cmp(generated, read, n, EPS):
    for i in range(0, n):
        if len(generated[i]) != len(read[i]):
            return False

        g_sorted = sorted(generated[i], key=lambda tuplu: tuplu[1])
        r_sorted = sorted(read[i], key=lambda tuplu: tuplu[1])

        for k in range(0, len(g_sorted)):
            if abs(g_sorted[k][0] - r_sorted[k][0]) >= EPS and g_sorted[k][1] != r_sorted[k][1]:
                print(g_sorted)
                print(r_sorted)
                return False
    return True


def list_cmp(generated, read, n, EPS):
    g_sorted = sorted(generated)
    r_sorted = sorted(read)

    for i in range(0, n):
        if abs(g_sorted[i][0][0] - r_sorted[i]) > EPS:
            return False
    return True


if __name__ == "__main__":
    """
        Reading from file
    """
    n, a, A = read_file("data/a.txt", True)
    n2, b, B = read_file("data/b.txt", True)
    n3, aplusb_input, AplusB_input = read_file("data/aplusb.txt", False)
    n4, aorib_input, AoriB_input = read_file("data/aorib.txt", False)

    """
        Generating the sum and the product of the matrices
    """
    if n == n2:
        AplusB_generated = matrix_sum(A, B, n)
        AoriB_generated = matrix_product(A, B, n)
    else:
        raise ValueError("Matrices do not have the same size")

    """
        Generating the results
    """
    x = []
    for i in range(n, 0, -1):
        x.append([[i, 0]])
    b_generated = matrix_product(B, x, n)

    """
        Print the outputs
    """
    if list_cmp(b_generated, b, n, 0.00001):
        print("Generated list 'B*x' = input list 'B*x'")
    else:
        print("Generated list 'B*x' != input list 'B*x'")

    if matrix_cmp(AplusB_generated, AplusB_input, n, 0.0001):
        print("Generated matrix 'A+B' = input matrix 'A+B'")
    else:
        print("Generated matrix 'A+B' != input matrix 'A+B'")

    if matrix_cmp(AoriB_generated, AoriB_input, n, 0.0001):
        print("Generated matrix 'A*B' = input matrix 'A*B'")
    else:
        print("Generated matrix 'A*B' != input matrix 'A*B'")
