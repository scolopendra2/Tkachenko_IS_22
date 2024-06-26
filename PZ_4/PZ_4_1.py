"""Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
целые степени числа A от 1 до N.
"""


def main():
    a = input('Введите вещественное число:')
    while '.' not in a:
        print('ERROR это не вещественное число')
        a = input('Введите вещественное число:')
    n = input('Введите целое число:')
    while not n.isdigit():
        print('ERROR это не число')
        n = input('Введите целое число:')
    print('Все целые степени числа A от 1 до N:')
    for i in range(1, int(n) + 1):
        print(float(a) ** i)


if __name__ == '__main__':
    main()
