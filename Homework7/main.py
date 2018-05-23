"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""

import numpy as np


def read_from_file(file_path):
    fd = open(file_path, 'rb')
    values = {}
    """ Read the values of the function """
    while True:
        line = fd.readline()
        array = line.split()
        if len(array) < 2:
            break
        values[float(array[0])] = float(array[1])
    """ Get value of n """
    line = fd.readline().strip()
    n_array = line.decode().split('=')
    if len(n_array) < 2:
        return False, None, None, None, None, None
    n = int(n_array[1])
    """ Get value of x0 """
    line = fd.readline().strip()
    x0_array = line.decode().split("=")
    if len(x0_array) < 2:
        return False, None, None, None, None, None
    x0 = float(x0_array[1])
    """ Get value of xn """
    line = fd.readline().strip()
    xn_array = line.decode().split("=")
    if len(xn_array) < 2:
        return False, None, None, None, None, None
    xn = float(xn_array[1])
    """ Get value of x """
    line = fd.readline().strip()
    x_array = line.decode().split("=")
    if len(x_array) < 2:
        return False, None, None, None, None, None
    x = float(x_array[1])

    return True, values, n, x0, xn, x


def progressive_newton(values, n, x0, xn, x):
    if xn < x0:
        return False, None
    h = (xn - x0) / (n - 1)
    """ Determine the interpolation points """
    x_interpol = [0] * (n)
    x_interpol[0] = x0
    for i in range(1, n):
        x_interpol[i] = x0 + i * h
    """ Determine t """
    t = (x - x0) / h
    """ Start computing L """
    y = [0] * (n)
    s = [0] * (n)
    y[0] = values[x0]
    s[0] = 1
    s[1] = t
    L = 0

    """ First step """
    for index in range(1, n):
        y[index] = values[list(values.keys())[index + 1]] - values[list(values.keys())[index]]

    """ Following steps """
    for step in range(2, n):
        s[step] = s[step - 1] * (t - step + 1) / step

        z = [0] * (n - step)
        for index in range(0, n - step):
            z[index] = y[step + index] - y[step + index - 1]
        for index in range(0, n - step):
            y[step + index] = z[index]

    """ Compute L """
    for index in range(0, n):
        L += s[index] * y[index]

    return True, L


# def interpol_smallest_squares(values, n, x0, xn, x):
#     if xn < x0:
#         return False, None
#
#     h = (xn - x0) / (n - 1)
#
#     """ Determine the interpolation points """
#     x_interpol = [0] * (n)
#     x_interpol[0] = x0
#
#     for i in range(1, n):
#         x_interpol[i] = x0 + i * h
#
#     # Construct the polynome something like: S(x) = a1*pow(x, 4) + a2*pow(x,3) + a3*pow(x,2) + a4*pow(x,1) + a5
#     # Construct the coefficient matrix
#     # For each of the interpolation values
#     coeff_matrix = np.empty([n, n])
#     result_array = np.empty(n)
#     for line_index in range(0, 5):
#         for col_index in range(0, 5):
#             coeff_matrix[line_index][col_index] = pow(x_interpol[line_index], 4 - col_index)
#         result_array[line_index] = values[x_interpol[line_index]]
#
#     # Determine the a coefficient array
#     a = np.linalg.solve(coeff_matrix, result_array)
#     # Determine the value in the point based on Horner's scheme
#     d = np.empty(n)
#     d[0] = a[0]
#
#     for i in range(1, n):
#         d[i] = a[i] + d[i - 1] * x
#
#     result = d[n - 1]
#     return True, result


if __name__ == '__main__':
    check, values, n, x0, xn, x = read_from_file("input.txt")
    if check:
        check, result = progressive_newton(values, n, x0, xn, x)
        if check:
            print("Result with progressive Newton: {0}".format(result))
        # check, result = interpol_smallest_squares(values, n, x0, xn, x)
        # if check:
        #     print("Result with least squares interpolation: {0}".format(result))
    else:
        print("Couldn't find result!")
