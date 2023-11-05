""".Из заданной строки отобразить только символы пунктуации. Использовать
библиотеку string.
Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"
"""
import string


def main():
    string_to_filter = r'--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'
    filtered_string = ''.join(character for character in string_to_filter if character in string.punctuation)
    print("Отфильтрованная строка:", filtered_string)


if __name__ == '__main__':
    main()
