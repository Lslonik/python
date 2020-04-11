# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# словарь с переводом
rus_numerals = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре"
}
result = []

# открываем файл и считываем данные оттуда
try:
    with open("HW_5.4_in.txt", "r") as my_file:
        for line in my_file:
            my_keys = line.split(" - ")  # преобразуем в список полученную строку
            if my_keys[0].lower() in rus_numerals:
                # заменяем на русс яз. версию
                result.append(f"{rus_numerals[my_keys[0].lower()].title()} - {my_keys[1]}")
except IOError:
    print("Ошибка чтения")

# открываем файл и записываем туда результат
try:
    with open("HW_5.4_out.txt", "w", encoding="utf-8") as my_file:
        my_file.writelines(result)
except IOError:
    print("Ошибка записи")
