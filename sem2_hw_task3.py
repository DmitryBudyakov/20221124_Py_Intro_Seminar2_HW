# Задача 3
# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.  
# Пример:  
# Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

title = 'Список из n чисел последовательности (1+1/n)^n и его сумма'
print('-'*len(title))
print(title)
print('-'*len(title))

def calc_function(num):
    return (1 + 1/num)**num

n = int(input('Введите целое число n: '))

nums = []

# добавление в список результатов вычисления по формуле
for i in range(1, n+1):
    nums.append(calc_function(i))

# сумма всех элементов списка
sum_of_nums = sum(nums)

print(f'для n = {n}: {nums}')
print(f'сумма = {sum_of_nums}')
    