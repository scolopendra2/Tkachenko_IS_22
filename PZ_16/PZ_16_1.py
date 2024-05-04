"""Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
Добавьте методы для сложения, вычитания и умножения матриц."""

import random


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для вычитания.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для умножения.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * other.data[i][j]
        return result


if __name__ == '__main__':
    matrix_1 = Matrix(3, 3)
    matrix_2 = Matrix(3, 3)
    print(matrix_1)
    print()
    print(matrix_2)
    matrix_add = matrix_1 + matrix_2
    print()
    print(matrix_add)
    matrix_subtract = matrix_1 - matrix_2
    print()
    print(matrix_subtract)
    matrix_multiply = matrix_1 * matrix_2
    print()
    print(matrix_multiply)
