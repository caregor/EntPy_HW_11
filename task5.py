# ------------------------------------------- 5 -----------------------------
"""
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""


class Rectangle:

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def __repr__(self):
        return f' Rectangle ({ self.height =}, {self.width =})'

    def perimeter(self):
        """
        Primetr of Rectangle.
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Area of Rectangle
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Add of rectangles.
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Sub Rectangles
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)
