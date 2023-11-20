"""С помощью функций получить вертикальную и горизонтальную линии. Линия
проводится многократной печатью символа. Заключить слово в рамку из
полученных линий."""


def vert_line(k):
    return '|   ' + ' ' * k + '   |\n'


def vert_line_with_word(word):
    return '|   ' + word + '   |\n'


def goriz_line(k):
    return '____' + '_' * k + '____\n'


def create_ramka(word):
    k = len(word)
    return (goriz_line(k) +
            vert_line(k) +
            vert_line(k) +
            vert_line(k) +
            vert_line_with_word(word) +
            vert_line(k) +
            vert_line(k) +
            vert_line(k) +
            goriz_line(k))


def main():
    word = input('Введите слово:')
    print(create_ramka(word))


if __name__ == '__main__':
    main()
