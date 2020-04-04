# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_division(dividend, divider):
    """
    функция выполняющая деление двух принятых чисел
    :param dividend: число которое делим
    :param divider: число которое делит
    :return: в случае удачи возвращает результат деления, иначе сообщение об ошибке
    """
    try:
        return int(dividend) / int(divider)
    except ZeroDivisionError:
        return 'Делитель не должен быть равен 0'
    except ValueError:
        return 'Вводить можно только числа!'


# запрос делимого числа
dividend_input = input('Введите делимое число: ')
# запрос делителя
divider_input = input('Введите делитель числа: ')

print(my_division(dividend_input, divider_input))
