"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def square_coat(self):
        return f"Площадь на пальто: {round(self.v / 6.5 + 0.5, 2)}"

    @property
    def square_suit(self):
        return f"Площадь на костюм: {round(self.h * 2 + 0.3, 2)}"

    @property
    def square_clothes(self):
        return f"Общая площадь: {round(((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)), 2)}"


class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.coatSquare = round((self.v / 6.5 + 0.5), 2)

    def __str__(self):
        return f"Площадь на пальто {self.coatSquare}"


class Suit(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.suitSquare = round((self.v * 2 + 0.3), 2)

    def __str__(self):
        return f"Площадь на костюм {self.suitSquare}"


MyCoat = Coat(1.72, 0.7)
print(MyCoat.square_clothes)
print(MyCoat.square_coat)
print(MyCoat.__str__())

MySuit = Suit(1.81, 0.9)
print(MySuit.square_clothes)
print(MySuit.square_coat)
print(MySuit.__str__())
