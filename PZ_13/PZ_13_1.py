"""Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE."""


def main():
    matrix = [[-1, -2, -3, -4, -5],
              [-6, -7, -8, -9, -10],
              [-11, -12, -13, -14],
              [16, -17, -18, -19, -20]]
    result_list = list(map(lambda x: any(list(map(lambda y: y > 0, x))), matrix))
    print(any(result_list))


if __name__ == '__main__':
    main()
