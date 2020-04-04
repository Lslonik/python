# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(first_number, second_number, third_number):
    """
    функция считает сумму наибольших аргументов
    :param first_number: первое число
    :param second_number: второе число
    :param third_number: третье число
    :return: ничего не возвращает и сразу выводит на экран
    # переводим в список чтобы воспользоваться функцией max
    # списох чтобы сохранить наибольшие числа, чтобы потом использовать функцию sum
    # ищем 1ое максимальное число
    # записываем в список для подсчета суммы
    # удаляем из списка аргументов 1е максимально число чтобы найти 2е максимальное
    # добавляем в список для подсчета суммы и потом выводим сумму чисел
    # находим второе максимальное число
    """
    my_list = [first_number, second_number, third_number]
    my_sum = []
    max_number = max(my_list)
    my_sum.append(max_number)
    my_list.remove(max_number)
    max_number = max(my_list)
    my_sum.append(max_number)
    print(sum(my_sum))


my_func(-1, -2, 4)
