"""Дан словарь на 6 персон, найти и вывести их средний возраст. (Пример,
{"Андрей": 32, "Виктор": 29, "Максим": 18, …}, среднее 26,33)."""


def main():
    my_dict = {
        'Андрей': 32, 'Виктор': 29, 'Максим': 18,
        'Петя': 30, 'Вася': 25, 'Загидин': 17
    }
    print(f'Средний возраст: {sum(my_dict.values()) / len(my_dict)}')


if __name__ == '__main__':
    main()
