"""Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел."""


def main():
    a = input('Введите 1 число:')
    while not a.isdigit():
        print('ERROR это не число')
        a = input('Введите 1 число:')
    b = input('Введите 2 число:')
    while not b.isdigit():
        print('ERROR это не число')
        b = input('Введите 2 число:')
    c = input('Введите 3 число:')
    while not c.isdigit():
        print('ERROR это не число')
        c = input('Введите 3 число:')
    a, b, c = int(a), int(b), int(c)
    if a > b and a > c:
        print(f'Наибольшее число {a}')
    elif b > a and b > c:
        print(f'Наибольшее число {b}')
    else:
        print(f'Наибольшее число {c}')
    if a < b and a < c:
        print(f'Наименьшее число {a}')
    elif b < a and b < c:
        print(f'Наименьшее число {b}')
    else:
        print(f'Наименьшее число {c}')


if __name__ == '__main__':
    main()
