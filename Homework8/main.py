"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""
import math

h = pow(10, -3)
kmax = 10000
polynome = [1, -6, 13, -12, 4]


def f(x):
    return x ** 2 - 4 * x + 3


def derivative(x):
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)


def secant(x0, x1, EPS):
    for k in range(kmax):
        nominator = (x1 - x0) * derivative(x1)
        denominator = derivative(x1) - derivative(x0)

        if math.fabs(denominator) < EPS:
            dx = pow(10, -5)
        else:
            dx = nominator / denominator
        x1 = x1 - dx

        if k > kmax:
            raise Exception("Divergenta la iteratia: {0}\n".format(k))
        elif math.fabs(dx) > pow(10, 8):
            raise Exception("abs(dx) > 10^8!\n")
        if math.fabs(dx) < EPS:
            return x1


def muller(R, EPS):
    k = 3
    sol = []
    import random
    x0 = random.randint(0, R)
    x1 = random.randint(0, R)
    x2 = random.randint(0, R)
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
        if max_b < EPS:
            raise Exception("Values smaller than epsilon!\n")
        delta_x = 2 * c / max_b
        x3 = x2 - delta_x
        k += 1
        x0 = x1
        x1 = x2
        x2 = x3
        if delta_x < EPS and x2 not in sol:
            sol.append(x2)
        if k > kmax or delta_x > pow(10, 8):
            break

    return sol


def horner(x):
    acc = 0
    for c in reversed(polynome):
        acc = acc * x + c
    return acc


if __name__ == '__main__':

    R = (abs(polynome[0]) + max(polynome)) / abs(polynome[0])
    print('Interval is: [' + str(-R) + ', ' + str(R) + ']')

    solutions = muller(R, 0.0000001)
    print('Found ' + str(len(solutions)) + ' roots')

    for i, r in enumerate(solutions):
        print('x' + str(i) + ' = ' + str(r))

    print("\nLocal minimum:")
    x0 = -0.4
    print("\tx0 = " + str(x0))
    x1 = -0.5
    print("\tx1 = " + str(x1))
    x = secant(x0, x1, 0.0000001)
    print("\tSecant(x0,x1) = " + str(x))
