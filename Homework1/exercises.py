import random


def ex1():
    try:
        u = 1
        output = u
        while 1:
            assert (u / 10), output
            u = u / 10
            if 1 + u != 1:
                #    print("The number is: ", u)
                output = u

    except Exception as e:
        print("THE WORKING LIMIT: ", e)
        return output / 10


def ex2_a():
    x = 1.0
    y = ex1()
    z = ex1()

    sum1 = (x + y) + z
    sum2 = x + (y + z)

    return sum1 == sum2


def ex2_b():
    x = random.random()
    y = ex1()
    z = ex1()

    prod1 = (x * y) * z
    prod2 = x * (y * z)

    while prod1 == prod2:
        x = random.random()
        prod1 = (x * y) * z
        prod2 = x * (y * z)

    print("Multiplication not associative for x = ", x, "and y,z = ", y)

    return x
