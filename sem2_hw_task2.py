# Задача 2
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

title = 'Набор произведений чисел от 1 до N'
print('-'*len(title))
print(title)
print('-'*len(title))

n = int(input('Введите натуральное число N: '))

nums = []
count = 1
for i in range(n):
    if i == 0:
        nums.append(1)
    else:
        nums.append(count*nums[i - 1])
    count += 1

print(f'при N = {n} -> {nums}')
