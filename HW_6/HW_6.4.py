# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


# класс Car, имеет атрибуты speed, color, name, is_police, метода go() stop() turn() show_speed() police() what_color()
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # функция go возвращает какая машина поехала
    def go(self):
        return f'{self.name} поехала'

    # функция stop возвращает какая машина остановилась
    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, turn_direction):
        """Функция turn

        :param turn_direction: получаем данные о том куда повернули
        :return: возвращает какая машина куда повернула
        """
        return f'{self.name} повернула {turn_direction}'

    # функция show_speed возвращает какая скорость у какой машины
    def show_speed(self):
        return f'скорость машины {self.name}: {self.speed}'

    # Функция police возвращает является ли машина полицейской
    def police(self):
        return f'манина {self.name} полицейская' if self.is_police else f'манишна {self.name} не полицейская'

    # Функция what_color возвращает какого цвета машина
    def what_color(self):
        return f'цвет машины {self.name}: {self.color}'


# класс TownCar, дочерний класс от класса Car
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)  # для работы с атрибутами родителя, перечисляем их

    # функция show_speed возвращает скорость машины если она не больше 60, иначе выдаем сообщение о превышении
    def show_speed(self):
        return f'скорость {self.name} превышает 60км/ч, скорость: {self.speed}км/ч' if self.speed > 60 else \
            f'скорость машины {self.name}: {self.speed}'


# класс TownCar, дочерний класс от класса Car
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)  # для работы с атрибутами родителя, перечисляем их


# класс TownCar, дочерний класс от класса Car
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)  # для работы с атрибутами родителя, перечисляем их

    # функция show_speed возвращает скорость машины если она не больше 40, иначе выдаем сообщение о превышении
    def show_speed(self):
        return f'скорость {self.name} превышает 40км/ч, скорость: {self.speed}км/ч' if self.speed > 40 else \
            f'скорость машины {self.name}: {self.speed}'


# класс TownCar, дочерний класс от класса Car
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)  # для работы с атрибутами родителя, перечисляем их


# создаем экземпляры
lada = PoliceCar(60, 'синяя', 'Vesta', True)
bmw = TownCar(90, 'черная', 'X5', False)
mazda = WorkCar(44, 'зеленая', 'Mazda 3', True)
ferarri = SportCar(150, 'красная', 'Laferrari', False)

# вывод на экран
print(lada.go())
print(lada.turn('направо'))
print(lada.show_speed())
print(lada.stop())
print(lada.what_color())
print(f'{lada.police()}\n')

print(bmw.go())
print(bmw.turn('налево'))
print(bmw.show_speed())
print(bmw.stop())
print(bmw.what_color())
print(f'{bmw.police()}\n')

print(mazda.go())
print(mazda.turn('направо'))
print(mazda.show_speed())
print(mazda.stop())
print(mazda.what_color())
print(f'{mazda.police()}\n')

print(ferarri.go())
print(ferarri.show_speed())
print(ferarri.turn('налево'))
print(ferarri.stop())
print(ferarri.what_color())
print(f'{ferarri.police()}\n')
