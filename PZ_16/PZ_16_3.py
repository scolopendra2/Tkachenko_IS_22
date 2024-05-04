"""Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате."""

import pickle

from PZ_16_1 import Matrix


def save_def(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    file_name = 'data_matrix.bin'
    matrix_1 = Matrix(3, 3)
    matrix_2 = Matrix(3, 3)
    matrix_add = matrix_1 + matrix_2
    matrixs = [matrix_1, matrix_2, matrix_add]
    save_def(matrixs, file_name)
    matrixs = load_def(file_name)
    for matrix in matrixs:
        print(matrix)
        print()
