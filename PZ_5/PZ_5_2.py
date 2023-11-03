"""С помощью функций получить вертикальную и горизонтальную линии. Линия
проводится многократной печатью символа. Заключить слово в рамку из
полученных линий."""


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
