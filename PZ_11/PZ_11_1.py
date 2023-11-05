"""Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов:
Количество элементов первого и второго файлов:
Элементы последней трети:
Индекс максимального элемента последней трети:"""


def main():
    with open('data_PZ_11/one_file.txt', 'w', encoding='utf8') as file:
        file.write('1, 2, 3, 4, -1, -2, -3, -4')
    with open('data_PZ_11/two_file.txt', 'w', encoding='utf8') as file:
        file.write('5, 6, 7, 8, -5, -6, -7, -8')
    one_file = open('data_PZ_11/one_file.txt', 'r', encoding='utf8')
    one_file_data = one_file.readline().split(', ')
    one_file.close()
    two_file = open('data_PZ_11/two_file.txt', 'r', encoding='utf8')
    two_file_data = two_file.readline().split(', ')
    two_file.close()
    all_data = one_file_data + two_file_data
    result = list()
    result.append(f'Элементы первого и второго файлов: {", ".join(all_data)}')
    result.append(f'Количество элементов первого и второго файлов: {len(all_data)}')
    all_data = list(map(lambda x: int(x), all_data))
    elements_last_tret = all_data[len(all_data) * 2//3:]
    result.append(f'Элементы последней трети: {elements_last_tret}')
    result.append(f'Индекс максимального элемента последней трети: {elements_last_tret.index(max(elements_last_tret))}')
    with open('data_PZ_11/result_data.txt', 'w', encoding='utf8') as file:
        file.write('\n'.join(result))


if __name__ == '__main__':
    main()