"""Из предложенного текстового файла (text18-32.txt) вывести на экран его содержимое,
количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
который поместить текст в стихотворной форме предварительно вставив после каждой
строки строку из символов «*»."""


def main():
    file = open('data_PZ_11/text18-32.txt', 'r', encoding='utf16')
    file_data = list(map(lambda x: x.strip(), file.readlines()))
    file.close()
    print('\n'.join(file_data))
    data_count = ''.join(file_data[:4])
    count = data_count.count('.') + data_count.count('!') + data_count.count(',') + data_count.count('?')
    print(f'Количество знаков пунктуации в первых четырёх строках: {count}')
    max_symbols = max(list(map(lambda x: len(x), file_data)))
    with open('data_PZ_11/new_file.txt', 'w', encoding='utf8') as file:
        file.write(f'\n{"*" * max_symbols}\n'.join(file_data))


if __name__ == '__main__':
    main()
