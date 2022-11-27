# Задача 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли).
# Пример:
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

title = 'Произведение элементов на указанных позициях списка [-N, N]'
sub_title = '(решение для ввода позиций с консоли)'
print('-'*len(title))
print(title)
print(sub_title)
print('-'*len(title))

def create_list(num):
    nums = []
    for i in range(-num, num + 1):
        nums.append(i)
    return nums

n = int(input('Введите натуральное число N для создания списка [-N, N]: '))

num_list = create_list(n)
print(f'при N = {n} -> {num_list}')

nums_length = len(num_list)

ids = list(map(int, input(f'Введите номера позиций от 0 до {nums_length-1}, \
которые надо перемножить [напр.: 0,1]: ').split(',')))

# проверка индекса (не должен превышать длину списка чисел)
for id in ids:
    if id > nums_length-1:
        print(f'Error: введен неверный индекс {id}')
        exit()

# перемножение элементов списка по заданным индексам
mult = 1
for i in range(len(ids)):
    mult *= num_list[ids[i]]

print(f'Позиции: {ids} -> {mult}')
