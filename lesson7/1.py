"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, arr1, arr2):
        self.matrix = [arr1, arr2]
        self.arr1 = arr1
        self.arr2 = arr2

    def __str__(self):
        print(
            str('\n'.join(['\t'.join([str(a) for a in b]) for b in self.matrix]))
        )

    def __add__(self):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for a in range(len(self.arr1)):

            for b in range(len(self.arr2[a])):
                matrix[a][b] = self.arr1[a][b] + self.arr2[a][b]

        print(
            str('\n'.join(['\t'.join([str(b) for b in a]) for a in matrix]))
        )


MyMatrix = Matrix([[5, 18, 11], [6, 17, 23], [41, 50, 9]], [[45, 8, 2], [6, 7, 93], [24, 5, 97]])

MyMatrix.__str__()
MyMatrix.__add__()