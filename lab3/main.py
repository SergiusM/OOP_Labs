
"""
Создать класс Array3d, который будет представлять трехмерный массив,
но на самом деле будет хранить данные в одномерном массиве. Вот список методов, которые нужно реализовать:
Создание экземпляра класса Array3d с заданными размерами (dim0, dim1, dim2)
Индексатор для доступа к элементам массива по трехмерным координатам (i, j, k)
Метод GetValues0(int i): возвращает срез массива по первой координате (i, .., ..).
Метод GetValues1(int j): возвращает срез массива по второй координате (.., j, ..).
Метод GetValues2(int k): возвращает срез массива по третьей координате (.., .., k).
Метод GetValues01(int i, int j): возвращает срез массива по первой и второй координатам (i, j, ..)
Метод GetValues02(int i, int k): возвращает срез массива по первой и третьей координатам (i, .., k)
Метод GetValues12(int j, int k): возвращает срез массива по второй и третьей координатам (.., j, k)
Метод SetValues0(int i, [][]): устанавливает значения в массиве для заданной первой координаты
Метод SetValues1(int j, [][]): устанавливает значения в массиве для заданной второй координаты
Метод SetValues2(int k, [][]): устанавливает значения в массиве для заданной третьей координаты
Метод SetValues01(int i, int j, [][]): устанавливает значения в массиве для заданных первой и второй координат
Метод SetValues02(int i, int k, [][]): устанавливает значения в массиве для заданных первой и третьей координат
Метод SetValues12(int j, int k, [][]): устанавливает значения в массиве для заданных второй и третьей координат
Методы для создания массива с одинаковыми элементами: ones, zeros,fill
"""
class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.dim0 = dim0
        self.dim1 = dim1
        self.dim2 = dim2
        self.data = [None] * (dim0 * dim1 * dim2)

    def __getitem__(self, indices):
        i, j, k = indices
        return self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k]

    def __setitem__(self, indices, value):
        i, j, k = indices
        self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = value

    def GetValues0(self, i):
        slice = []
        for j in range(self.dim1):
            for k in range(self.dim2):
                slice.append(self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k])
        return slice

    def GetValues1(self, j):
        slice = []
        for i in range(self.dim0):
            for k in range(self.dim2):
                slice.append(self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k])
        return slice

    def GetValues2(self, k):
        slice = []
        for i in range(self.dim0):
            for j in range(self.dim1):
                slice.append(self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k])
        return slice

    def GetValues01(self, i, j):
        slice = []
        for k in range(self.dim2):
            slice.append(self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k])
        return slice

    def GetValues02(self, i, k):
        slice = []
        for j in range(self.dim1):
            slice.append(self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k])
        return slice

    def GetValues12(self, j, k):
        slice = []
        for i in range(self.dim0):
            slice.append(self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k])
        return slice

    def SetValues0(self, i, arr):
        for j in range(self.dim1):
            for k in range(self.dim2):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = arr[j][k]

    def SetValues1(self, j, arr):
        for i in range(self.dim0):
            for k in range(self.dim2):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = arr[i][k]

    def SetValues2(self, k, arr):
        for i in range(self.dim0):
            for j in range(self.dim1):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = arr[i][j]

    def SetValues01(self, i, j, arr):
        for k in range(self.dim2):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = arr[k]

    def SetValues02(self, i, k, arr):
        for j in range(self.dim1):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = arr[j]

    def SetValues12(self, j, k, arr):
        for i in range(self.dim0):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = arr[i]


def ones(dim0, dim1, dim2):
    arr = Array3d(dim0, dim1, dim2)
    for i in range(dim0):
        for j in range(dim1):
            for k in range(dim2):
                arr[i, j, k] = 1
    return arr


def zeros(dim0, dim1, dim2):
    arr = Array3d(dim0, dim1, dim2)
    for i in range(dim0):
        for j in range(dim1):
            for k in range(dim2):
                arr[i, j, k] = 0
    return arr


def fill(dim0, dim1, dim2, value):
    arr = Array3d(dim0, dim1, dim2)
    for i in range(dim0):
        for j in range(dim1):
            for k in range(dim2):
                arr[i, j, k] = value
    return arr

# Создание массива с единичными элементами
arr_ones = ones(3, 3, 3)
print(arr_ones.GetValues0(0))  # Возвращает срез массива по первой координате (i, .., ..)
print(arr_ones.GetValues1(1))  # Возвращает срез массива по второй координате (.., j, ..)
print(arr_ones.GetValues2(2))  # Возвращает срез массива по третьей координате (.., .., k)
print(arr_ones.GetValues01(0, 1))  # Возвращает срез массива по первой и второй координатам (i, j, ..)
print(arr_ones.GetValues02(0, 2))  # Возвращает срез массива по первой и третьей координатам (i, .., k)
print(arr_ones.GetValues12(1, 2))  # Возвращает срез массива по второй и третьей координатам (.., j, k)

# Создание массива с нулевыми элементами
arr_zeros = zeros(2, 2, 2)
print(arr_zeros.GetValues0(1))
print(arr_zeros.GetValues1(0))
print(arr_zeros.GetValues2(1))
print(arr_zeros.GetValues01(1, 0))
print(arr_zeros.GetValues02(1, 1))
print(arr_zeros.GetValues12(0, 1))

# Создание массива с заданным значением
arr_fill = fill(2, 3, 4, 5)
print(arr_fill.GetValues0(1))
print(arr_fill.GetValues1(2))
print(arr_fill.GetValues2(3))
print(arr_fill.GetValues01(1, 2))
print(arr_fill.GetValues02(1, 3))
print(arr_fill.GetValues12(2, 3))

arr = Array3d(3, 4, 5)

values = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

arr.SetValues0(1, values)

print(arr.GetValues0(1))
