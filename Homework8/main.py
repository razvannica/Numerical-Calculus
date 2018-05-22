"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import math
import numpy as np
import cmath

sol = []

epsilon = pow(10, -9)
h = pow(10, -3)
kmax = 10000
polyn = [-1, 1, -1]


def f(x):
    return x ** 2 - 4 * x + 3


def f_2(x):
    return x ** 2 + np.exp(x)


def f_1(x):
    return x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4


def deriv1(x):
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)


def deriv2(x):
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def der_ord2(x):
    return -f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h) / (12 * h ** 2)


def secanta(x0, x1):
    for k in range(kmax):
        nominator = (x1 - x0) * deriv1(x1)
        denominator = deriv1(x1) - deriv1(x0)
        if math.fabs(denominator) < epsilon:
            dx = pow(10, -5)
        else:
            dx = nominator / denominator
        x1 = x1 - dx

        if k > kmax:
            print("Divergenta la iteratia: {0}\n".format(k))
            return None
        elif math.fabs(dx) > pow(10, 8):
            print("Explozie!\n")
            return None
        if math.fabs(dx) < epsilon:
            return x1


def mp(x):
    p = np.poly1d(polyn)
    return p(x)


def poly_to_string(p, fd):
    toprint = []
    for i, coef in enumerate(p, 1):
        if coef == 0:
            continue
        if coef >= 0 and i != 1:
            toprint.append(' + ')
        elif coef < 0:
            toprint.append(' - ')
        toprint.append(str(np.abs(coef)))
        if i != len(p):
            toprint.append('x^' + str(len(p) - i))

    pstring = 'Polynomial: {0}'.format(''.join(toprint))
    fd.write(pstring + "\n")
    print(pstring)
    return True


def muller_complex(x0, x1, x2):
    k = 3
    while True:
        h0 = x1 - x0
        h1 = x2 - x1
        if h1 == 0 or h0 == 0:
            break
        ro_0 = (horner(x1) - horner(x0)) / h0
        ro_1 = (horner(x2) - horner(x1)) / h1
        a = (ro_1 - ro_0) / (h1 + h0)
        b = a * h1 + ro_1
        c = horner(x2)
        max_b = (b.real ** 2 + b.imag ** 2) + cmath.sqrt((b.real ** 2 + b.imag ** 2)**2
                                                         - 4*a*c*(b.conjugate().real**2 + b.conjugate().imag**2))
        if abs(max_b.real) < epsilon < epsilon:
            print("Values smaller than epsilon!\n")
            break
        delta_x = 2 * c*b.conjugate() / max_b
        x3 = x2 - delta_x
        k += 1
        x0 = x1
        x1 = x2
        x2 = x3
        if abs(delta_x.real) < epsilon and x2 not in sol:
            sol.append(x2)
        if k > kmax or delta_x.real > pow(10, 8):
            break

    return sol


def muller(x0, x1, x2):
    k = 3
    while True:
        h0 = x1 - x0
        h1 = x2 - x1
        if h1 == 0 or h0 == 0:
            break
        ro_0 = (horner(x1) - horner(x0)) / h0
        ro_1 = (horner(x2) - horner(x1)) / h1
        a = (ro_1 - ro_0) / (h1 + h0)
        b = a * h1 + ro_1
        c = horner(x2)
        if b ** 2 - 4 * a * c < 0:
            print("Nu am identificat radacini reale!\n")
            return muller_complex(complex(x0 + 0j), complex(x1 + 0j), complex(x2 + 0j))
        max_b = max(b + math.sqrt(b ** 2 - 4 * a * c), b - math.sqrt(b ** 2 - 4 * a * c))
        if max_b < epsilon:
            print("Values smaller than epsilon!\n")
            break
        delta_x = 2 * c / max_b
        x3 = x2 - delta_x
        k += 1
        x0 = x1
        x1 = x2
        x2 = x3
        if delta_x < epsilon and x2 not in sol:
            sol.append(x2)
        if k > kmax or delta_x > pow(10, 8):
            break

    return sol


def horner(x):
    acc = 0
    for c in reversed(polyn):
        acc = acc * x + c
    return acc


if __name__ == '__main__':
    """" Use secant method to determine local min """
    """ x0 = -0.4
    x1 = -0.5
    x = secanta(x0, x1)
    print(x) """

    with open('output.txt', 'w') as fd:
        """ Write polynom to file """
        poly_to_string(polyn, fd)

        """ Determine roots interval """
        R = (abs(polyn[0]) + max(polyn)) / abs(polyn[0])
        R_int_str = 'Interval is: [{0}, {1}]'.format(-R, R)
        print(R_int_str)
        fd.write(R_int_str + "\n")

        """ Determine solutions """
        sols = muller(0, 1, 2)
        rstring = 'Found {0} roots'.format(len(sols))
        print(rstring)
        fd.write(rstring + '\n')
        for i, r in enumerate(sols):
            rstring = 'x{0} = {1}'.format(i, r)
            print(rstring)
            fd.write(rstring + '\n')
        fd.write('\n')
