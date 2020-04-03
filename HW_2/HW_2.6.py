# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# переменные для хранения данных и для выхода с цикла
products = []
analytic = {}
end_get = None


while end_get != 'exit':
    # запрос на ввод номера
    number_product = input('Введите номер для нового продукта: ')
    end = None
    specification = {}
    # в цикле создаем словарь с описанием товара
    while end != 'exit':
        specification_key = input('Введите название характеристики: ').lower()
        specification_val = input('Введите описание характеристики: ').lower()
        specification[specification_key] = specification_val
        end = input('Продолжить ввод характеристик? для выхода введите exit иначе любое значение: ')
    # в список добавляем кортеж из номера товара и кортежа характеристик
    products.append(tuple([number_product, specification]))
    end_get = input('Чтобы завершить ввод товаров введите exit: ')

print(f'Наш словарь с номером и описаниями товаров: {products}')

# производим анализ, перебор каждого кортежа
for product in products:
    # product[1].items() берем индекс 1, под этим индексом лежит словарь
    for specification_key, specification_val in product[1].items():
        if specification_key in analytic:
            # если есть такой ключ в словаре, то к его значениям в списке добавляем новое значение
            analytic[specification_key].append(specification_val)
        else:
            # если ключа нет в словаре аналитик, то добавляет ключ и значение его ввиде списка
            analytic[specification_key] = [specification_val]

print(f'Наш новый словарь после анализа: {analytic}')
