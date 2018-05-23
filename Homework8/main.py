"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import math
import numpy

sol = []

epsilon = pow(10, -9)
h = pow(10, -3)
kmax = 10000
polyn = [2, 2, -1]


def f(x):
    return x ** 2 - 4 * x + 3


# def f_2(x):
#     return x ** 2 + numpy.exp(x)


# def f_1(x):
#     return x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4


def deriv1(x):
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)


# def deriv2(x):
#     return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


# def der_ord2(x):
#     return -f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h) / (12 * h ** 2)


def secant(x0, x1):
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


def poly_to_string(p, fd):
    toprint = []
    for i, coef in enumerate(p, 1):
        if coef == 0:
            continue
        if coef >= 0 and i != 1:
            toprint.append(' + ')
        elif coef < 0:
            toprint.append(' - ')
        toprint.append(str(numpy.abs(coef)))
        if i != len(p):
            toprint.append('x^' + str(len(p) - i))

    pstring = 'Polynomial: {0}'.format(''.join(toprint))
    fd.write(pstring + "\n")
    print(pstring)
    return True


def muller(x0, x1, x2):
    k = 3
    while True:
        h0 = x1 - x0
        h1 = x2 - x1
        if h1 == 0 or h0 == 0:
            break
        ro_0 = (horner(x1) - horner(x0)) / h0
        ro_1 = (horner(x2) - horner(x1)) / h1
        try:
            a = (ro_1 - ro_0) / (h1 + h0)
        except Exception:
            break
        b = a * h1 + ro_1
        c = horner(x2)
        max_b = max(b + math.sqrt(b ** 2 - 4 * a * c), b - math.sqrt(b ** 2 - 4 * a * c))
        if max_b < epsilon:
            raise Exception("Values smaller than epsilon!\n")
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

    """" Use secant method to determine local min """
    print("\nSecant method to determine local minimum:")
    x0 = -0.4
    print("\tx0 = " + str(x0))
    x1 = -0.5
    print("\tx1 = " + str(x1))
    x = secant(x0, x1)
    print("\tsecant(x0,x1) = " + str(x))
