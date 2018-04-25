"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""

import copy


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


def product_with_array(A, size):
    C = []
    x = [value for value in range(size, 0, -1)]
    for index in range(0, size):
        sum = 0

        for A_line in A[index]:
            val_x = x[A_line[1]]
            sum += A_line[0] * val_x

        C.append(sum)
    return C
