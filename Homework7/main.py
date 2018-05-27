"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""


def read_from_file(file_path):
    fd = open(file_path, 'rb')
    values = {}

    while True:
        line = fd.readline()
        array = line.split()
        if len(array) < 2:
            break
        values[float(array[0])] = float(array[1])

    line = fd.readline().strip()
    n_array = line.decode().split('=')
    if len(n_array) < 2:
        raise Exception("Issue at reading from file!")
    n = int(n_array[1])

    line = fd.readline().strip()
    x0_array = line.decode().split("=")
    if len(x0_array) < 2:
        raise Exception("Issue at reading from file!")
    x0 = float(x0_array[1])

    line = fd.readline().strip()
    xn_array = line.decode().split("=")
    if len(xn_array) < 2:
        raise Exception("Issue at reading from file!")
    xn = float(xn_array[1])

    line = fd.readline().strip()
    x_array = line.decode().split("=")
    if len(x_array) < 2:
        raise Exception("Issue at reading from file!")
    x = float(x_array[1])

    return values, n, x0, xn, x


def progressive_newton(values, n, x0, xn, x):
    if xn < x0:
        raise Exception("xn<x0")
    h = (xn - x0) / (n - 1)

    x_interpol = [0] * (n)
    x_interpol[0] = x0
    for i in range(1, n):
        x_interpol[i] = x0 + i * h
    t = (x - x0) / h

    y = [0] * (n)
    s = [0] * (n)
    y[0] = values[x0]
    s[0] = 1
    s[1] = t
    L = 0

    for index in range(1, n):
        y[index] = values[list(values.keys())[index + 1]] - values[list(values.keys())[index]]

    for step in range(2, n):
        s[step] = s[step - 1] * (t - step + 1) / step

        z = [0] * (n - step)
        for index in range(0, n - step):
            z[index] = y[step + index] - y[step + index - 1]
        for index in range(0, n - step):
            y[step + index] = z[index]

    for index in range(0, n):
        L += s[index] * y[index]

    return L


if __name__ == '__main__':
    values, n, x0, xn, x = read_from_file("input.txt")
    result = progressive_newton(values, n, x0, xn, x)
    if not result:
        print("Couldn't find result!")
    print("Progressive Newton: " + str(result))
