# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    """Класс Date, имеет атрибут users_date, классметод extract, статикметод valid"""
    def __init__(self, users_date):
        self.users_date = users_date

    @classmethod
    def extract(cls, users_date):
        """Метод извлекает число месяц год и преобразовывает их к типу число

        :param users_date: Принимаемая строка
        :return: возвращает кортеж из чисел
        """
        result = []
        users_date = users_date.split('-')  # из строки делаем список

        for i in users_date:  # перебираем список и если элемент не равен пробелу добавляем в result
            if i != ' ':
                result.append(i)
        return int(result[0]), int(result[1]), int(result[2])

    @staticmethod
    def valid(day, month, year):
        """Метод принимает число месяц и год, и проверяет их на валидность

        :param day: число
        :param month: месяц
        :param year: год
        :return: возвращает сообщение все хорошо если дата валидна, иначе ошибку
        """
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year >= 0:
                    return 'Данные введены корректно'
                else:
                    return 'Год введен не правильно'
            else:
                return 'Месяц введен не правильно'
        else:
            return 'День введен не правильно'

    def __str__(self):
        # возвращает нашу извлеченную дату
        return f'Сегоднящняя дата {Date.extract(self.users_date)}'


# экземпляр класса
today = Date('21-04-2020')

# выводы
print(today)
print(today.extract('21-04-2020'))
print(Date.extract('21 - 04 - 2020'))
print(Date.valid(21, 4, 2020))
print(Date.valid(21, 14, 2020))
print(Date.valid(41, 12, 2020))
print(Date.valid(21, 12, -2020))
