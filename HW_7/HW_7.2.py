# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

# импортируем  ABC и abstractmethod из модуля abc
from abc import ABC, abstractmethod


# класс Clothes имеет атрибуты size height, и методы get_full_square get_square_coat get_square_costume
class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height
    
    @property
    def get_full_square(self):
        return f'Площадь ткани необходимой всего: {round(((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)), 2)}'

    @abstractmethod
    def get_square_coat(self):
        pass

    @abstractmethod
    def get_square_costume(self):
        pass


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def get_square_coat(self):
        return round((self.size / 6.5 + 0.5), 2)

    def get_square_costume(self):
        pass


class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def get_square_costume(self):
        return round((self.height * 2 + 0.3), 2)

    def get_square_coat(self):
        pass


my_costume = Costume(1, 4)
my_coat = Coat(4, 7)

print(my_costume.get_square_costume())
print(my_coat.get_square_coat())

print(my_costume.get_full_square)
print(my_coat.get_full_square)

