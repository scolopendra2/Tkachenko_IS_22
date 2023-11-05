""".Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
количество полученных элементов.
"""
import re


def main():
    with open('experience.txt', 'r', encoding='utf8') as file:
        data_file = file.readlines()[2:]
    pattern = r"(\d+ (год|лет|года) \d+ месяц|\d+ (год|лет|года)|\d+ месяц)"
    matches = re.findall(pattern, ''.join(data_file))
    print(f'Количество полученных элементов: {len(matches)}')


if __name__ == '__main__':
    main()