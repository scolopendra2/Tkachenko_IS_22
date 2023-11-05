"""Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE."""


def main():
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14],
              [16, 17, 18, 19, 20]]
    new_matrix = list(map(lambda x: True if True in list(filter(lambda y: y > 0, x)) else False, matrix))
    print(True if True in new_matrix else False)


if __name__ == '__main__':
    main()
