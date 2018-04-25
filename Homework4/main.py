"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import read_from_file
import h4
import numpy

EPS = 0.00001

for index in range(0, 5):
    print("Matrix " + str(index + 1) + ":")
    size, b, A = read_from_file.read_file("data/m_rar_2018_" + str(index + 1) + ".txt", True)
    if h4.main_diagonal_validation(A, size, EPS):
        iter1, xg1 = h4.gauss_siedel(A, b, size, EPS)
        if iter1:
            print("\tIterations: " + str(iter1), xg1[:6])
            print("\tInducted matrix norm: " + str(
                max(abs(i) for i in numpy.subtract(h4.product_with_array(A, xg1, size), b))))
        else:
            print("\tMatrix " + str(index + 1) + " is disjoint")
    else:
        print("\tValues are null on main diagonal of matrix " + str(index + 1))
