# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

number = int(input('Введите количесво чисел: '))
result = 0

# открываем файл и записываем в него рандомные числа начиная от 1 до указанного пользователем
try:
    my_file = open("HW_5.5_out.txt", "w")
    for i in range(1, number + 1):
        my_file.write(f"{randint(1, number)} ")
except IOError:
    print("Ошибка записи")
finally:
    my_file.close()

# тут считываем с файла числа и считаем их сумму, если элемент пустая строка то не учитываем
try:
    my_file = open("HW_5.5_out.txt", "r")
    my_list = my_file.read()
    print(f'Список чисел из файла: {my_list}')
    for elem in my_list:
        if elem != ' ':
            result += int(elem)
    print(f'Сумма чисел из файла равна: {result}')
except IOError:
    print("Ошибка чтения")
finally:
    my_file.close()
