import math
from math import pi
from math import sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = [*color] if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False

    def get_color(self):  # Готово
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in [r, g, b])

    def set_color(self, r, g, b):  # Готово
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):  # Готово
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):  # Готово
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)


class Triangle(Figure):  # Готово
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.calculate_height()

    def calculate_height(self):
        s = sum(self.get_sides()) / 2
        area = (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5
        return 2 * area / self.get_sides()[0]

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__height = self.calculate_height()


class Cube(Figure):  # Готово
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, *sides * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def set_sides(self, *sides):
        if len(sides) == 1:
            super().set_sides(*sides * 12)


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
