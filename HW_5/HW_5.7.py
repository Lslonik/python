# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

inform_firm = []

with open("HW_5.7_in.txt", "r") as my_file:
    sum_of_profit = 0
    count = 0
    my_dict = {}
    my_average_prof = {}
    for el in my_file:
        profit = 0
        title, type_of_ownership, earnings, costs = el.split()
        profit = int(earnings) - int(costs)
        if profit > 0:
            sum_of_profit += profit
            count += 1
        my_dict[title] = profit
    inform_firm.append(my_dict)
    my_average_prof['average_profit'] = sum_of_profit / count
    inform_firm.append(my_average_prof)

with open("HW_5.7_out.json", "w") as my_file:
    json.dump(inform_firm, my_file)






