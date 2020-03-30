# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

set_true = True
# словарь хранящий номер месяца и название
month = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}

# список со временем года
seasons = ['Зима', 'Весна', 'Лето', 'Осень']

# Сначала проверяем входную цифру, если это не цифра просим ввести цифру и запрашиваем заново ввод
# если ввели цифру меньше 1 и больше 12 просим ввести цифру в этом диапазоне и сново запрашиваем цифру
# как только ввели корректные данные выводим результат на экран и заверщаем программу
while set_true:
    try:
        # запращиваем номер месяца
        users_number_of_month = int(input('Введите пожалуйста номер месяца от 1 до 12: '))
    except ValueError:
        print('Введите пожалуйста цифру')
        continue

    if 1 <= users_number_of_month <= 12:
        keys_of_dict = month.get(users_number_of_month)
        if users_number_of_month == 12 or users_number_of_month == 1 or users_number_of_month == 2:
            your_month_season = seasons[0]
        elif users_number_of_month == 3 or users_number_of_month == 4 or users_number_of_month == 5:
            your_month_season = seasons[1]
        elif users_number_of_month == 6 or users_number_of_month == 7 or users_number_of_month == 8:
            your_month_season = seasons[2]
        else:
            your_month_season = seasons[3]
        print(f'Вы выбрали месяц {keys_of_dict} под номером {users_number_of_month} и '
              f'ваш месяц относиться к времени года {your_month_season}')
        set_true = False
    else:
        print('Введите цифру от 1 до 12')


