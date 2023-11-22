"""Создаем базовый абстрактный класс для численного расчета интегралов, у которого есть метод Calc, 
в который передайте подынтегральное выражение в виде функции, верхнюю, нижнюю границу. 
Сам класс имеет параметры; число точек, шаг, точность. 
Строим два производных класса для расчета интегралов методом трапеций и методом Симпсона,
Демонстрируете успешность работы классов на примеру взятия интеграла 
результат которого вы можете посчитать аналитически
"""
import abc

class Quadrature(metaclass=abc.ABCMeta):
    def __init__(self, num_points, step, precision):
        self.num_points = num_points
        self.step = step
        self.precision = precision

    @abc.abstractmethod
    def calc(self, f, a, b):
        pass
#расчет методом трапеций
class TrapezoidalQuadrature(Quadrature):
    def calc(self, f, a, b):
        if self.num_points < 1 or self.step <= 0 or self.precision <= 0:
            raise ValueError("Некорректные параметры")
        
        h = (b - a) / self.num_points
        integral = (f(a) + f(b)) / 2
        
        for i in range(1, self.num_points):
            x = a + i * h
            integral += f(x)
        
        integral *= h
        return integral
    
#расчет методом Симпсона
class SimpsonQuadrature(Quadrature):
    def calc(self, f, a, b):
        if self.num_points < 2 or self.step <= 0 or self.precision <= 0:
            raise ValueError("Некорректные параметры")
        
        if self.num_points % 2 != 0:
            self.num_points += 1
        
        h = (b - a) / self.num_points
        integral = f(a) + f(b)
        
        for i in range(1, self.num_points):
            x = a + i * h
            if i % 2 == 0:
                integral += 2 * f(x)
            else:
                integral += 4 * f(x)
        
        integral *= h / 3
        return integral

# Пример использования классов
def f(x):
    return x ** 0.5

#ввод верхней и нижней границ
up_bound = 1
down_bound = 0

trapezoidal = TrapezoidalQuadrature(num_points=100, step=0.01, precision=0.0001)
trapezoidal_result = trapezoidal.calc(f, down_bound, up_bound)

simpson = SimpsonQuadrature(num_points=100, step=0.01, precision=0.0001)
simpson_result = simpson.calc(f, down_bound, up_bound)

print("Результат метода трапеций:", trapezoidal_result)
print("Результат метода Симпсона:", simpson_result)

