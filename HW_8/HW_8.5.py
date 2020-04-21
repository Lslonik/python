class MyComplexNumber:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return f'{self.number_1 + other.number_1} + {self.number_2 + other.number_2}i'

    def __mul__(self, other):
        return f'{(self.number_1 * other.number_1) - (self.number_2 * other.number_2)} + ' \
               f'{(self.number_1 * other.number_2) + (self.number_2 * other.number_1)}i'

    def __str__(self):
        return f'{self.number_1} + {self.number_2}i'


first_number = MyComplexNumber(2, 1)
second_number = MyComplexNumber(3, 4)
print(f'Первое комплексное число: {first_number}')
print(f'Второе комплексное число: {second_number}')

print(f'Результат сложения: {first_number + second_number}')
print(f'Результат умножения: {first_number * second_number}')
