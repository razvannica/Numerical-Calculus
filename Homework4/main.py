"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import read_from_file
import h4
import numpy

n1, b1, A1 = read_from_file.read_file("data/m_rar_2018_1.txt", True)
n2, b2, A2 = read_from_file.read_file("data/m_rar_2018_2.txt", True)
n3, b3, A3 = read_from_file.read_file("data/m_rar_2018_3.txt", True)
n4, b4, A4 = read_from_file.read_file("data/m_rar_2018_4.txt", True)
n5, b5, A5 = read_from_file.read_file("data/m_rar_2018_5.txt", True)
EPS = 0.00001

m_rar = [
    [n1, b1, A1],
    [n2, b2, A2],
    [n3, b3, A3],
    [n4, b4, A4],
    [n5, b5, A5]
]

index = 1
for case in m_rar:
    if h4.main_diagonal_validation(case[2], case[0], EPS):
        iter1, xg1 = h4.gauss(case[2], case[1], case[0], EPS)
        if iter1:
            print("Matrix" + str(index) + ":")
            print("Iterations" + str(iter1), xg1[:6])
            print("Inducted matrix norm" + str(
                max(abs(i) for i in numpy.subtract(h4.product_with_array(case[2], xg1, n1), case[1]))))
        else:
            print("Matrix " + str(index) + " is disjoint")
    else:
        print("Values are null on main diagonal of matrix " + str(index))