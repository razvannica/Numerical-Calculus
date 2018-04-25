"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import read_from_file
import h4
import time
import numpy

EPS = 0.00001

for index in range(0, 5):
    print("\nMatrix " + str(index + 1) + ":")

    """ Reading from file """
    size, b, A = read_from_file.read_file("data/m_rar_2018_" + str(index + 1) + ".txt", True)

    if h4.main_diagonal_validation(A, size):
        """ Searching for solutions with gauss_siedel """
        t0 = time.time()
        iterations, xg = h4.gauss_siedel(A, b, size, EPS)
        t1 = time.time()

        """ Printing the outputs """
        if iterations != 0:
            print("\tNumber of iterations: " + str(iterations))
            print("\tInducted matrix norm: " + str(
                max(abs(i) for i in numpy.subtract(h4.product_with_array(A, xg, size), b))))
            print("\tTime: " + str(t1 - t0))
        else:
            print("\tMatrix " + str(index + 1) + " is disjoint")

    else:
        print("\tThere are null values on the main diagonal of matrix " + str(index + 1))
