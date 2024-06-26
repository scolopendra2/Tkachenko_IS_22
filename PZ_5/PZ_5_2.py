"""Описать функцию SortDec3(A, B, C), меняющую содержимое переменных A, B, C
таким образом, чтобы их значения оказались упорядоченными по убыванию (A, B,
C — вещественные параметры, являющиеся одновременно входными и
выходными). С помощью этой функции упорядочить по убыванию два данных
набора из трех чисел: (A1, B1, C1) и (A2, B2, C2)."""


def sortdec3(a, b, c):
    a, b, c = a, b, c
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b
    return a, b, c


def main():
    print(sortdec3(1.5, 1.3, 3.7))
    print((sortdec3(9.1, 3.3, 5.4)))


if __name__ == '__main__':
    main()
