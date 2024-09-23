import math
from math import pi
from math import sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):  # Готово
        self.__sides = sides
        self.__color = color
        self.filled = False

    def get_color(self):  # Готово
        return list(self.__color)

    @staticmethod
    def __is_valid_color(r, g, b):  # Готово
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r in range(256) and g in range(256) and b in range(256):
                return True
            return False

    def set_color(self, r, g, b):  # Готово
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    @staticmethod
    def __is_valid_sides(*sides):   # Готово
        if all(isinstance(side, int) and side > 0 for side in sides):
            return True
        return False

    def get_sides(self):  # Готово
        if len(self.__sides) != self.sides_count:
            return [1] * self.sides_count
        else:
            return self.__sides

    def __len__(self):   # Переделать
        return sum(self.__sides)

    def set_sides(self, *new_sides):   # Готово
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(*new_sides):
                self.__sides = list(new_sides)
        else:
            self.__sides = [*self.__sides] * self.sides_count


class Circle(Figure):   # Готово
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        circle_side = sides[0]
        self.__radius = circle_side / (2 * pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Triangle(Figure):  # Готово
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == Triangle.sides_count:
            self.a = sides[0]
            self.b = sides[1]
            self.c = sides[2]
            self.s = (self.a + self.b + self.c) / 2

    def get_square(self):
        return math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


class Cube(Figure):   # Готово
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.cube_side = sides[0]

    def get_volume(self):
        return self.cube_side ** 3

    def perimeter(self):
        return self.cube_side * 12


# Проверка
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 35, 130), 8, 3, 6)  # Добавлен для проверки
#
# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
#
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
print(cube1.get_volume())
print(circle1.get_square())
print(triangle1.get_square())  # Добавлен для проверки
