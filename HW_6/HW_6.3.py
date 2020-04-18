# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


# класс Worker имеет атрибуты name, surname, position, wage, bonus
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


# класс Position, дочерний класс от класса Worker имеет методы get_full_name, get_position, get_total_income
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)  # для работы с атрибутами родителя, перечисляем их

    # функция get_full_name возвращает полное имя сотрудника
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    # функция get_position возвращает должность
    def get_position(self):
        return self.position

    # функция get_total_income возвращает доход с учетом бонуса
    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


# создаем экземпляры
my_worker = Position('Катя', 'Андреева', 'Бухгалтер', 25000, 10000)

# вывод на экран
print(my_worker.get_full_name())
print(my_worker.get_position())
print(my_worker.get_total_income())
