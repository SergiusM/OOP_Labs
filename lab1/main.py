
import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vector:
    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[1].x - args[0].x
            self.y = args[1].y - args[0].y
            self.z = args[1].z - args[0].z
        elif len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)
    
    def normalize(self):
        magnitude = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return Vector(self.x / magnitude, self.y / magnitude, self.z / magnitude)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross_product(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)
    
    def scalar_multiply(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def is_collinear(self, other):
        cross_product = self.cross_product(other)
        return cross_product.length() == 0
    
    def is_coplanar(self, other1, other2):
        cross_product = self.cross_product(other1)
        return cross_product.is_collinear(other2)
    
    def distance(self, other):
        displacement = self - other
        return displacement.length()

while True:
    print("1. Создать вектор по координатам")
    print("2. Создать вектор по двум точкам")
    print("3. Сложение векторов")
    print("4. Вычитание векторов")
    print("5. Получить обратный вектор")
    print("6. Построить единичный вектор")
    print("7. Вычислить скалярное произведение векторов")
    print("8. Вычислить векторное произведение векторов")
    print("9. Проверить коллинеарность векторов")
    print("10. Проверить компланарность векторов")
    print("11. Вычислить расстояние между векторами")
    print("12. Вычислить угол между векторами")
    print("0. Выход")
    
    choice = int(input("Введите номер операции: "))
    
    if choice == 0:
        break
    
    if choice == 1:
        x = float(input("Введите координату x: "))
        y = float(input("Введите координату y: "))
        z = float(input("Введите координату z: "))
        vector = Vector(x, y, z)
        print(f"Создан вектор: {vector}")
    
    if choice == 2:
        x1 = float(input("Введите координату x первой точки: "))
        y1 = float(input("Введите координату y первой точки: "))
        z1 = float(input("Введите координату z первой точки: "))
        x2 = float(input("Введите координату x второй точки: "))
        y2 = float(input("Введите координату y второй точки: "))
        z2 = float(input("Введите координату z второй точки: "))
        
        point1 = Point(x1, y1, z1)
        point2 = Point(x2, y2, z2)
        
        vector = Vector(point1=point1, point2=point2)
        print(f"Создан вектор: {vector}")
    
    if choice == 3:
        x1 = float(input("Введите координату x первого вектора: "))
        y1 = float(input("Введите координату y первого вектора: "))
        z1 = float(input("Введите координату z первого вектора: "))
        x2 = float(input("Введите координату x второго вектора: "))
        y2 = float(input("Введите координату y второго вектора: "))
        z2 = float(input("Введите координату z второго вектора: "))
        
        vector1 = Vector(x1, y1, z1)
        vector2 = Vector(x2, y2, z2)
        
        result = vector1.__add__(vector2)
        print(f"Результат сложения: {result}")
    if choice == 4:
        x1 = float(input("Введите координату x первого вектора: "))
        y1 = float(input("Введите координату y первого вектора: "))
        z1 = float(input("Введите координату z первого вектора: "))
        x2 = float(input("Введите координату x второго вектора: "))
        y2 = float(input("Введите координату y второго вектора: "))
        z2 = float(input("Введите координату z второго вектора: "))
        
        vector1 = Vector(x1, y1, z1)
        vector2 = Vector(x2, y2, z2)
        
        result = vector1.__sub__(vector2)
        print(f"Результат вычитания: {result}")
        
    if choice == 5:
        x = float(input("Введите координату x вектора: "))
        y = float(input("Введите координату y вектора: "))
        z = float(input("Введите координату z вектора: "))
        
        vector = Vector(x, y, z)
        
        result = vector.__neg__()
        print(f"Обратный вектор: {result}")
    
    if choice == 6:
        x = float(input("Введите координату x вектора: "))
        y = float(input("Введите координату y вектора: "))
        z = float(input("Введите координату z вектора: "))
        
        vector = Vector(x, y, z)
        
        result = vector.normalize()
        print(f"Единичный вектор: {result}")
    
    if choice == 7:
        x1 = float(input("Введите координату x первого вектора: "))
        y1 = float(input("Введите координату y первого вектора: "))
        z1 = float(input("Введите координату z первого вектора: "))
        x2 = float(input("Введите координату x второго вектора: "))
        y2 = float(input("Введите координату y второго вектора: "))
        z2 = float(input("Введите координату z второго вектора: "))
        
        vector1 = Vector(x1, y1, z1)
        vector2 = Vector(x2, y2, z2)
        
        result = vector1.dot_product(vector2)
        print(f"Скалярное произведение: {result}")
    
    if choice == 8:
        x1 = float(input("Введите координату x первого вектора: "))
        y1 = float(input("Введите координату y первого вектора: "))
        z1 = float(input("Введите координату z первого вектора: "))
        x2 = float(input("Введите координату x второго вектора: "))
        y2 = float(input("Введите координату y второго вектора: "))
        z2 = float(input("Введите координату z второго вектора: "))
        
        vector1 = Vector(x1, y1, z1)
        vector2 = Vector(x2, y2, z2)
        
        result = vector1.cross_product(vector2)
        print(f"Векторное произведение: {result}")
    
    if choice == 9:
        x1 = float(input("Введите координату x первого вектора: "))
        y1 = float(input("Введите координату y первого вектора: "))
        z1 = float(input("Введите координату z первого вектора: "))
        x2 = float(input("Введите координату x второго вектора: "))
        y2 = float(input("Введите координату y второго вектора: "))
        z2 = float(input("Введите координату z второго вектора: "))
        
        vector1 = Vector(x1, y1, z1)
        vector2 = Vector(x2, y2, z2)
        
        result = vector1.is_collinear(vector2)
        if result:
            print("Векторы коллинеарны")
        else:
            print("Векторы неколлинеарны")
    
    if choice == 10:
        x1 = float(input("Введите координату x первого вектора: "))
        y1 = float(input("Введите координату y первого вектора: "))
        z1 = float(input("Введите координату z первого вектора: "))
        x2 = float(input("Введите координату x второго вектора: "))
        y2 = float(input("Введите координату y второго вектора: "))
        z2 = float(input("Введите координату z второго вектора: "))
        
        vector1 = Vector(x1, y1, z1)
        vector2 = Vector(x2, y2, z2)
        
        result = vector1.is_coplanar(vector2)
        if result:
            print("Векторы компланарны")
        else:
            print("Векторы некомпланарны")
    
    if choice == 11:
        x1 = float(input("Введите координату x первого вектора: "))
        y1 = float(input("Введите координату y первого вектора: "))
        z1 = float(input("Введите координату z первого вектора: "))
        x2 = float(input("Введите координату x второго вектора: "))
        y2 = float(input("Введите координату y второго вектора: "))
        z2 = float(input("Введите координату z второго вектора: "))
        
        vector1 = Vector(x1, y1, z1)
        vector2 = Vector(x2, y2, z2)
        
        result = vector1.distance(vector2)
        print(f"Расстояние между векторами: {result}")
    
    if choice == 12:
        x1 = float(input("Введите координату x первого вектора: "))
        y1 = float(input("Введите координату y первого вектора: "))
        z1 = float(input("Введите координату z первого вектора: "))
        x2 = float(input("Введите координату x второго вектора: "))
        y2 = float(input("Введите координату y второго вектора: "))
        z2 = float(input("Введите координату z второго вектора: "))
        
        vector1 = Vector(x1, y1, z1)
        vector2 = Vector(x2, y2, z2)
        
        result = vector1.angle(vector2)
        print(f"Угол между векторами: {result}")
