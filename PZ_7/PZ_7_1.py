"""Даны строки S и S0. Удалить из строки S первую подстроку, совпадающую с S0. Если
совпадающих подстрок нет, то вывести строку S без изменений."""


def main():
    s = 'Python one love'
    s0 = 'love'
    s = s.replace(s0, '')
    print(s)


if __name__ == '__main__':
    main()
    