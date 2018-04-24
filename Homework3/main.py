"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""

import read_from_file
import h3

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
        if abs(g_sorted[i] - r_sorted[i]) > EPS:
            return False
    return True


"""
    Reading from file
"""

n, a, A = read_from_file.read_file("data/a.txt", True)
n2, b, B = read_from_file.read_file("data/b.txt", True)
n3, csumfromtxt, Csumfromtxt = read_from_file.read_file("data/aplusb.txt", False)
n4, cprodfromtxt, Cprodfromtxt = read_from_file.read_file("data/aorib.txt", False)

"""
    Generating the sum and the product of the matrices
"""
Csum = h3.matrix_sum(A, B, n)
Cprod = h3.matrix_product(A, B, n)

"""
    Generating the results
"""
a_generated = h3.product_with_array(A, n)
b_generated = h3.product_with_array(B, n)
sum_generated = h3.product_with_array(Csumfromtxt, n)
prod_generated = h3.product_with_array(Cprodfromtxt, n)

"""
    Print the outputs
"""
if list_cmp(a_generated, a, n, 0.00001):
    print("Generated list 'a' = input list 'a'")
else:
    print("Generated list 'a' != input list 'a'")

if list_cmp(b_generated, b, n, 0.00001):
    print("Generated list 'b' = input list 'b'")
else:
    print("Generated list 'b' != input list 'b'")

if list_cmp(sum_generated, csumfromtxt, n, 0.00001):
    print("Generated list 'a+b' = input list 'a+b'")
else:
    print("Generated list 'a+b' != input list 'a+b'")

if list_cmp(prod_generated, cprodfromtxt, n, 0.00001):
    print("Generated list 'a*b' = input list 'a*b'")
else:
    print("Generated list 'a*b' != input list 'a*b'")

if matrix_cmp(Csum, Csumfromtxt, n, 0.0001):
    print("Generated matrix 'A+B' = input matrix 'A+B'")
else:
    print("Generated matrix 'A+B' != input matrix 'A+B'")

if matrix_cmp(Cprod, Cprodfromtxt, n, 0.0001):
    print("Generated matrix 'A*B' = input matrix 'A*B'")
else:
    print("Generated matrix 'A*B' != input matrix 'A*B'")
