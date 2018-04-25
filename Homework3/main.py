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
n3, aplusb_input, AplusB_input = read_from_file.read_file("data/aplusb.txt", False)
n4, aorib_input, AoriB_input = read_from_file.read_file("data/aorib.txt", False)

"""
    Generating the sum and the product of the matrices
"""
AplusB_generated = h3.matrix_sum(A, B, n)
AoriB_generated = h3.matrix_product(A, B, n)

"""
    Generating the results
"""
a_generated = h3.product_with_array(A, n)
b_generated = h3.product_with_array(B, n)
sum_generated = h3.product_with_array(AplusB_input, n)
prod_generated = h3.product_with_array(AoriB_input, n)

"""
    Print the outputs
"""
if list_cmp(a_generated, a, n, 0.00001):
    print("Generated list 'A*x' = input list 'A*x'")
else:
    print("Generated list 'A*x' = input list 'A*x'")

if list_cmp(b_generated, b, n, 0.00001):
    print("Generated list 'B*x' = input list 'B*x'")
else:
    print("Generated list 'B*x' != input list 'B*x'")

if list_cmp(sum_generated, aplusb_input, n, 0.00001):
    print("Generated list '(A+B)*x' = input list '(A+B)*x'")
else:
    print("Generated list '(A+B)*x' != input list '(A+B)*x'")

if list_cmp(prod_generated, aorib_input, n, 0.00001):
    print("Generated list '(A*B)*x' = input list '(A*B)*x'")
else:
    print("Generated list '(A*B)*x' != input list '(A*B)*x'")

if matrix_cmp(AplusB_generated, AplusB_input, n, 0.0001):
    print("Generated matrix 'A+B' = input matrix 'A+B'")
else:
    print("Generated matrix 'A+B' != input matrix 'A+B'")

if matrix_cmp(AoriB_generated, AoriB_input, n, 0.0001):
    print("Generated matrix 'A*B' = input matrix 'A*B'")
else:
    print("Generated matrix 'A*B' != input matrix 'A*B'")
