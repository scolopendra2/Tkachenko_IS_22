"""Дан список размера N. Поменять местами его минимальный и максимальный
элементы."""


def main():
    my_list = [3, 45, 12, 58, 1, 23, 987, 123]
    min_in_list = min(my_list)
    max_in_list = max(my_list)
    min_index = my_list.index(min_in_list)
    max_index = my_list.index(max_in_list)
    my_list[min_index], my_list[max_index] = max_in_list, min_in_list
    print(f'Новый список: {my_list}')


if __name__ == '__main__':
    main()
