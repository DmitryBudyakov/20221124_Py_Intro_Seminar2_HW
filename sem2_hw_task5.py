# Задача 5
# Реализуйте алгоритм перемешивания списка.

from random import randint
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

title = 'Алгоритм перемешивания списка'
print('-'*len(title))
print(title)
print('-'*len(title))

# создание исходного списка [0,num]
def create_serial_list(num):
    nums = []
    for i in range(num):
        nums.append(i)
    return nums

# создание исходного списка random len(num)
def create_random_list(num, min_num = 0, max_num = 100):
    nums = []
    for i in range(num):
        nums.append(randint(min_num, max_num))
    return nums

# перемешивание списка
def list_shuffle(list):
    for i in range(len(list)):
        j = randint(0, i) # позиция, на которую перемещается i-й элемент
        temp = list[j]
        list[j] = list[i]
        list[i] = temp
    return list

n = int(input('Введите кол-во элементов в списке: '))

# исходный список для последовательного ряда чисел
init_list1 = create_serial_list(n)

# исходный список для random чисел
init_list2 = create_random_list(n)

# вывод исходного списка последовательного ряда чисел
title1 = 'Вариант 1: Ряд последовательных чисел'
print(title1)
print('-'*len(title1))
print(f'Исходный список:\t {init_list1}')
# перемешанный список последовательного ряда чисел
shuffled_list1 = list_shuffle(init_list1)
print(f'Перемешанный список:\t {shuffled_list1}')

print()
title2 = 'Вариант 2: Ряд случайных чисел'
print(title2)
print('-'*len(title2))
# если создавался список для random чисел
print(f'Исходный список:\t {init_list2}')
shuffled_list2 = list_shuffle(init_list2)
print(f'Перемешанный список:\t {shuffled_list2}')
