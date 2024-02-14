"""Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE."""


def main():
    matrix = [[i for i in range(j, j + 5)] for j in range(1, 19, 5)]
    print(matrix)
    print()
    result_list = list(map(lambda x: any(list(map(lambda y: y > 0, x))), matrix))
    print(any(result_list))


if __name__ == '__main__':
    main()
