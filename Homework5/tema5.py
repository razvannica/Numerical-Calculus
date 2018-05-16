import numpy as np

from homeworks.utils import print_matrix


def get_identity_matrix(n):
    _matrix = list()
    for _i in range(n):
        _sub_array = list()
        for _j in range(n):
            _sub_array.append(0 if _i != _j else 1)
        _matrix.append(_sub_array)

    return np.array(_matrix)


def get_initial_matrix(A):
    """
    Get V0, the initial matrix
    :param A: input matrix
    """
    _init_matrix = np.transpose(A)

    # get ||A||1
    _max_col_sum = 0
    for index in range(len(A[0])):
        _sum = sum([A[i][index] for i in range(len(A))])
        if _sum > _max_col_sum:
            _max_col_sum = _sum

    # get ||A||1
    _max_line_sum = 0
    for index in range(len(A)):
        _sum = sum([A[index][i] for i in range(len(A[index]))])
        if _sum > _max_line_sum:
            _max_line_sum = _sum

    _init_matrix /= (_max_line_sum * _max_col_sum)
    return _init_matrix


def the_shultz_way(A, V, I=None):  # the hyper-powah
    if I is None:
        I = get_identity_matrix(len(A))
    new_matrix = np.array(V)
    new_matrix *= (2 * I - A * V)
    return new_matrix


def first_li(A, V, I=None):  # the Li&Li iterative first meth-od
    if I is None:
        I = get_identity_matrix(len(A))

    new_matrix = np.array(V)
    new_matrix *= (3 * I - A * V * (3 * I - A * V))
    return new_matrix


def second_li(A, V, I=None):  # the Li&Li iterative second method
    if I is None:
        I = get_identity_matrix(len(A))

    new_matrix = np.array(V)
    new_matrix *= (I + 1.0 / 4.0 * (I - V * A) * (3 * I - V * A) * (3 * I - V * A))
    return new_matrix


def pb1(n, eps, kmax, A):
    """

    :param n: matrix dimension
    :param eps: calculus precision
    :param kmax: maximum number of iterations
    :param A: the non-singular nxn matrix
    :return: smth
    """
    _const = 10 ** 10
    _init_matrix = get_initial_matrix(A)

    run_all = {
        "shz": {
            "f": the_shultz_way,
            "V": _init_matrix.copy()
        },
        "li1": {
            "f": first_li,
            "V": _init_matrix.copy()
        },
        "li2": {
            "f": second_li,
            "V": _init_matrix.copy()
        }
    }

    _identity = get_identity_matrix(len(A))
    for cur_k in range(kmax):
        _remaining = len(run_all)

        for cur_way in run_all:
            if run_all[cur_way].get("done"):  # skip already finished
                _remaining -= 1
                continue

            _new_matrix = run_all[cur_way]["f"](A=A, V=run_all[cur_way]["V"], I=_identity)

            matrix_diff = np.linalg.norm(run_all[cur_way]["V"] - _new_matrix)
            run_all[cur_way]["norm"] = matrix_diff

            if eps <= matrix_diff <= _const:
                run_all[cur_way]["done"] = True

            run_all[cur_way]["V"] = _new_matrix

        if _remaining <= 0:
            break
    return run_all


if __name__ == '__main__':
    # print_matrix(get_identity_matrix(7))
    A = list([[1.0, 4.0, 0.0], [0.0, 1.0, 4.0], [0.0, 0.0, 1.0]])
    # _n = 10
    import random

    """for _n in range(10, 15):
        #A = [[0.0 for _j in range(_n)] for _i in range(_n)]
        for i in range(_n):
            A[i][i] = 1.0
            if i != _n-1:
                A[i][i+1] = 4.0
        print(A)"""
    _id = get_identity_matrix(len(A))
    res = pb1(3, 1**(-10), 10000, A)
    print(A)
    # print(res)
    for x in res:
        print(x)
        for _y in res[x]:
            print(_y)
            print(res[x][_y])
        print(x, np.linalg.norm(A * res[x]["V"] - _id, 1))
