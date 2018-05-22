"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""

import numpy
import copy

kmax = 1000000


def read_file(path, to_check):
    size = 0
    matrix = []

    with open(path) as file:
        k = 0

        for num, lines in enumerate(file, 1):

            if k == 0:
                size = int(lines.split()[0])
                k = 1
                matrix = [[] for i in range(0, size)]
            else:
                if lines != '\n' and k == 1:
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
    return size, matrix


def product_with_array(A, B, n):
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


def matrix_substract(A, B):
    size = len(A)
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
                C[C_line_index][C_index][0] -= B_line[0]
            else:
                C[C_line_index].insert(0, B_line)

    for C_line_index in range(0, size):
        if len(C[C_line_index]) > 20:
            raise ValueError("More than 20 null elements on line: " + str(C_line_index))
    return list()


def product_with_number(value, a_list, size):
    for i in range(0, size):
        a_list[i][0][0] *= value
    return a_list


def generate_list(size):
    x = []
    for i in range(size, 0, -1):
        x.append([[i, 0]])
    return product_with_number(1 / numpy.linalg.norm(x), x, len(x))


def pow_method(A, EPS):
    v = generate_list(len(A))

    w = product_with_array(A, v, len(A))

    _lambda = 0
    for index in range(len(v)):
        _lambda += v[index][0][0] * w[index][0][0]
    k = 0
    product = product_with_number(_lambda, v, len(v))

    while numpy.linalg.norm(matrix_substract(w, product)) > len(A) * EPS and k <= kmax:
        v = product_with_number(1 / numpy.linalg.norm(w, 2), w, len(w))
        w = product_with_array(A, v, len(A))

        for index in range(len(v)):
            _lambda += v[index][0][0] * w[index][0][0]

        k += 1
        product = product_with_number(_lambda, v, len(v))

    return _lambda, v


def check_empty_list_sparse(_list):
    for i in range(len(_list)):
        if len(_list[i]) == 0:
            return False
    return True


def generate_random_sparse_symmetric_matrix(size):
    from random import gauss, randint

    sparse = [[] for i in range(size)]
    for _ in range(size):
        (i, j) = (randint(0, size - 1), randint(0, size - 1))
        x = gauss(0, 1)
        # if not check_empty_list_sparse(sparse):
        if i != j:
            sparse[i].insert(0, [x, j])
            sparse[j].insert(0, [x, i])
        else:
            sparse[i].append([x, j])
            sparse[j].append([x, i])
        # else:
        #     break

    return sparse


def sparse_to_normal(sparse):
    to_return = [[0 for i in range(len(sparse))] for j in range(len(sparse))]

    for i in range(len(sparse)):
        for element in sparse[i]:
            to_return[i][element[1]] = element[0]

    return to_return


if __name__ == "__main__":
    print("Reading m_rar_sim_2018.")
    size, A = read_file("data/m_rar_sim_2018.txt", False)
    EPS = 0.00001

    print("\nComputing with pow method for m_rar_sim:")
    _lambda1, v1 = pow_method(A, EPS)
    print("\tlambda:\t", _lambda1)
    print("\tv:\t", v1)

    # print("\nGenerating random sparse symmetric matrix.")
    generated = generate_random_sparse_symmetric_matrix(5)
    #
    # print("\nComputing with pow method for generated sparse symmetric matrix:")
    # _lambda2, v2 = pow_method(generated, EPS)
    # print("\tlambda:\t", _lambda2)
    # print("\tv:\t", v2)

    matrix = sparse_to_normal(generated)
    U, s, V = numpy.linalg.svd(matrix)

    print("\n\n ------------- p>n -------------------")

    print('\nSingular values of the matrix: {}'.format([val for val in s]))
    print('Number of singular values for decomposition (rank): {}'.format(len(s)))
    print('Matrix rank: {}'.format(numpy.linalg.matrix_rank(matrix)))

    singular_vals = [val for val in s if val > 0]
    print('Condition number of matrix: {}'.format(max(singular_vals) / min(singular_vals)))
    print('Numpy condition number: {0}'.format(numpy.linalg.cond(matrix)))

    B = numpy.linalg.pinv(matrix)
    print("Moore-Penrose for the matrix: \n{0}".format(B))

    b = numpy.random.random(5)
    x = numpy.dot(B, b)
    # The solution is the Moore-Penrose pseudoinverse, multiplied by b
    print("Solution to Ax = b: {0}".format(x))

    s_val = int(input('s = '))
    while s_val > numpy.linalg.matrix_rank(matrix):
        print("s should be <= than ", numpy.linalg.matrix_rank(matrix))
        s_val = int(input('s = '))

    A_s = numpy.zeros(numpy.array(matrix).shape)
    for i in range(s_val):
        col_u = U[:, i]
        col_v = V[:, i]
        A_s += s[i] * numpy.dot(col_u.reshape(len(col_u), 1), col_v.reshape(1, len(col_v)))

    print("Value of matrix A_s: \n")
    print(A_s)
    print('Norm: {}'.format(numpy.linalg.norm(matrix - A_s, numpy.inf)))
