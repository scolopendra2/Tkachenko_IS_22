"""В последовательности на n целых чисел умножить все элементы на первый
максимальный элемент."""


def main():
    n = [1, 3, 45, 67, 1223, 5, 6, 2]
    max_element = max(n)
    n = list(map(lambda x: x * max_element, n))
    print(n)


if __name__ == '__main__':
    main()
