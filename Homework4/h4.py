"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import numpy
import copy


def norm(a_list, n):
    return (sum([(abs(a_list[i])) ** 2 for i in range(0, n)])) ** (0.5)


def main_diagonal_validation(A, n, EPS):
    for i in range(0, n):
        if A[i][len(A[i]) - 1][0] <= EPS:
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


def gauss_siedel(A, b, n, EPS):
    xc = [0 for i in range(0, n)]
    xp = [0 for i in range(0, n)]
    k = 0
    kmax = 10000
    # do start
    xc = compute_xc(xc, xp, b, A, n)
    xcnumpy = numpy.array(xc)
    xpnumpy = numpy.array(xp)
    deltax = norm(numpy.subtract(xcnumpy, xpnumpy), n)
    k += 1

    while deltax >= EPS and k <= kmax and deltax <= 10 ** 8:
        xp = copy.copy(xc)
        xc = compute_xc(xc, xp, b, A, n)
        xcnumpy = numpy.array(xc)
        xpnumpy = numpy.array(xp)
        deltax = norm(numpy.subtract(xcnumpy, xpnumpy), n)
        k += 1

    if deltax < EPS:
        return k, xc
    else:
        return 0, 0
