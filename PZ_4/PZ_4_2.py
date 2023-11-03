"""Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
деления, найти количество и сумму его цифр."""


def main():
    n = input('Введите целое число:')
    while not n.isdigit():
        print('ERROR это не число')
        n = input('Введите целое число:')
    all_numbers = len(n)
    sum_numbers = int(n) % 10
    for i in range(1, all_numbers):
        sum_numbers += int(n) // (10 ** i) % 10
    print(f'Длинна строки: {all_numbers}')
    print(f'Сумма цифр в строке: {sum_numbers}')


if __name__ == '__main__':
    main()