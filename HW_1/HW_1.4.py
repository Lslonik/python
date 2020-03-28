# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

set_true = True

while set_true:
    input_digit = input('Введите целое положительное число: ')  # запрос на ввод числа

    # переменные для цикла, в result сохраняем введенное число, на случай если ввели одну цифру
    i = len(input_digit) - 1
    result = input_digit

    # цикл while ищем с конца максимальную цифру
    if int(input_digit) > 0:
        while i >= 0:
            if int(input_digit[i]) < int(input_digit[i - 1]):
                result = input_digit[i - 1]
            i -= 1
        print(f'Максимальная цифра в числе: {result}')  # вывод результата
        set_true = False  # переключает set_true чтобы выйти с цикла while
    else:
        print(f'Вы ввели отрицательное число: {input_digit}.\nВведите пожалуйста целое положительное число')


