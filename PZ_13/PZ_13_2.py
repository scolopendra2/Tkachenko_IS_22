"""В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры)"""


def main():
    matrix = [[i for i in range(j, j + 5)] for j in range(1, 19, 5)]
    print(matrix)
    print()
    n = input('Введите строку матрицы:')
    while not n.isdigit():
        print('ERROR это не число')
        n = input('Введите строку матрицы:')
    print(f'Сумма элементов строки N: {sum(matrix[int(n)])}')
    proiz = 1
    for i in matrix[int(n)]:
        proiz *= i
    print(f'Произведение элементов строки N: {proiz}')


if __name__ == '__main__':
    main()
