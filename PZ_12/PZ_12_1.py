"""В последовательности на n целых чисел умножить все элементы на первый
максимальный элемент."""


def main():
    n = [i for i in range(1, 11)]
    max_element = max(n)
    n = list(map(lambda x: x * max_element, n))
    print(n)


if __name__ == '__main__':
    main()
