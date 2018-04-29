"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import numpy
import copy
import time

def read_file(path, is_generated):
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
                nr = float(line[0])
                index = int(line[1])
                j = int(line[2])

                if index == j:
                    ok = 0
                    for k in matrix[index]:
                        if len(k) > 1:
                            if k[1] == j:
                                k[0] += nr
                                ok = 1
                                break
                    if ok == 0:
                        matrix[index].append(list((nr, j)))
                else:
                    ok = 0
                    for k in matrix[index]:
                        if len(k) > 1:
                            if k[1] == j:
                                k[0] += nr
                                ok = 1
                                break
                    if ok == 0:
                        matrix[index].insert(0, list((nr, j)))

    if is_generated:
        for index in range(0, size):
            if len(matrix[index]) > 10:
                print(matrix[index])
                raise ValueError("The matrix has more than 10 inputs into line " + str(index))
    return size, input_list, matrix


def main_diagonal_validation(A, n):
    for i in range(0, n):
        if A[i][len(A[i]) - 1][0] == 0:
            return False
    return True


def product_with_array(A, x, n):
    C = []
    for index in range(0, n):
        sum = 0
        for A_list in A[index]:
            val_x = x[A_list[1]]
            sum += A_list[0] * val_x
        C.append(sum)
    return C


def norm(a_list, n):
    return numpy.linalg.norm(a_list, numpy.inf)


def compute_xc(xkplus1, xk, b, A, n):
    for i in range(0, n):
        sum1 = 0
        sum2 = 0
        for j in A[i]:
            if j[1] <= i - 1:
                sum1 += j[0] * xkplus1[j[1]]
            if j[1] >= i + 1:
                sum2 += j[0] * xk[j[1]]
        xkplus1[i] = (b[i] - sum1 - sum2) / A[i][len(A[i]) - 1][0]
    return xkplus1


def gauss_seidel(A, b, n, EPS):
    xc = [0 for i in range(0, n)]
    xp = [0 for i in range(0, n)]
    iterations = 0

    xc = compute_xc(xc, xp, b, A, n)
    delta_x = norm(
        numpy.subtract(numpy.array(xc), numpy.array(xp)), n
    )
    iterations += 1

    while EPS <= delta_x <= 10 ** 8 and iterations <= 10000:
        xp = copy.copy(xc)
        xc = compute_xc(xc, xp, b, A, n)
        delta_x = norm(
            numpy.subtract(numpy.array(xc), numpy.array(xp)), n
        )
        iterations += 1

    if delta_x < EPS:
        return iterations, xc
    else:
        return 0, 0


if __name__ == "__main__":

    EPS = 0.00001

    for index in range(0, 5):
        print("\nMatrix " + str(index + 1) + ":")

        """ Reading from file """
        size, b, A = read_file("data/m_rar_2018_" + str(index + 1) + ".txt", True)

        if main_diagonal_validation(A, size):
            """ Searching for solutions with gauss_seidel """
            t0 = time.time()
            iterations, xgs = gauss_seidel(A, b, size, EPS)
            t1 = time.time()

            """ Printing the outputs """
            if iterations != 0:
                print("\tNumber of iterations: " + str(iterations))
                print("\tInducted matrix norm: " + str(
                    max(abs(i) for i in numpy.subtract(product_with_array(A, xgs, size), b))))
                print("\tTime: " + str(t1 - t0))
                print("\tSolution xi= " + str(xgs[:5]))
            else:
                print("\tMatrix " + str(index + 1) + " is disjoint")

        else:
            print("\tThere are null values on the main diagonal of matrix " + str(index + 1))
