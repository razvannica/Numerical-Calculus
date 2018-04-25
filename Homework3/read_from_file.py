"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""


def read_file(path, to_check):
    size = 0
    input_list = []
    matrix = []

    with open(path) as file:
        k = 0

        for num, lines in enumerate(file, 1):
            if num < size + 3 and k != 0:
                try:
                    input_list.append(float(lines.split()[0]))
                except:
                    continue

            if k == 0:
                size = int(lines.split()[0])
                k = 1
                matrix = [[] for i in range(0, size)]

            if num > size + 3:
                line = lines.split(",")
                value = float(line[0])
                index_line = int(line[1])
                index_col = int(line[2])

                if index_line == index_col:
                    ok = 0
                    for matrix_line in matrix[index_line]:
                        if len(matrix_line) > 1:
                            if matrix_line[1] == index_col:
                                matrix_line[0] += value
                                ok = 1
                                break
                    if ok == 0:
                        matrix[index_line].append(list((value, index_col)))
                else:
                    ok = 0
                    for matrix_line in matrix[index_line]:
                        if len(matrix_line) > 1:
                            if matrix_line[1] == index_col:
                                matrix_line[0] += value
                                ok = 1
                                break
                    if ok == 0:
                        matrix[index_line].insert(0, list((value, index_col)))

    if to_check:
        for index_line in range(0, size):
            if len(matrix[index_line]) > 10:
                print(matrix[index_line])
                raise ValueError("The matrix has more than 10 inputs into line " + str(index_line))
    return size, input_list, matrix
