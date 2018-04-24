"""
Author: Răzvan NICA
Study Year: 3
Group: English
"""


def read_file(path, is_generated):
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
                nr = float(line[0])
                index = int(line[1])
                j = int(line[2])

                if index == j:
                    ok = 0
                    for k in matrix[index]:
                        if len(k) > 1:
                            if k[1] == j:
                                k[0] += nr
                                ok = 1
                                break
                    if ok == 0:
                        matrix[index].append(list((nr, j)))
                else:
                    ok = 0
                    for k in matrix[index]:
                        if len(k) > 1:
                            if k[1] == j:
                                k[0] += nr
                                ok = 1
                                break
                    if ok == 0:
                        matrix[index].insert(0, list((nr, j)))

    if is_generated:
        for index in range(0, size):
            if len(matrix[index]) > 10:
                print(matrix[index])
                raise ValueError("The matrix has more than 10 inputs into line " + str(index))
    return size, input_list, matrix
