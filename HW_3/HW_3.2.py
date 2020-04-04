# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# запращиваем данные пользователя
input_name = input('Введите имя пользователя: ')
input_surname = input('Введите фамилию пользователя: ')
input_year_of_birth = input('Введите дату рождения пользователя: ')
input_email = input('Введите электронну почту пользователя: ')
input_phone = input('Введите номер телефона пользователя: ')
input_city = input('Введите город проживания пользователя: ')


def users_data(name, surname, year_of_birth, city, email, phone):
    """
    Функция выводит данные пользователя в одну строчку
    :param name: принимает имя пользователя
    :param surname: принимает фамилию пользователя
    :param year_of_birth: принимает дату рождения
    :param city: принимает город проживания
    :param email: принимает электронную почту пользователя
    :param phone: принимает номер телефона
    :return: ничего не возвращает
    """
    print(name, surname, year_of_birth, city, email, phone)


users_data(input_name, input_surname, input_year_of_birth, input_city, input_email, input_phone)
