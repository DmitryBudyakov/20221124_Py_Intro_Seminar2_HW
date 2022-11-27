# Задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

title = 'Сумма цифр вещественного числа'
print('-'*len(title))
print(title)
print('-'*len(title))

# считает сумму цифр передаваемого числа
def summ_of_digits(number):
    summa = 0
    while number != 0:
        summa += number % 10
        number //= 10
    return summa

def is_dot_or_comma(text):
    if text.count('.') == 1:
        return 1
    elif text.count(',') == 1:
        return 0
    else:   # нет дробной части, введено целое число
        return -1
        
num = input('Введите вещественное число [напр: 0.56]: ')

# проверяем как введено вещественное число, с точкой или запятой
# если с запятой, заменяем на точку
if is_dot_or_comma(num) == 0:
    num = num.replace(',','.')

# разделяем целую и дробную часть в список в виде int
num_list = list(map(int, num.split('.')))

sum_total = 0
# считаем сумму цифр каждого элемента списка и суммируем
for value in num_list:
    sum_total += summ_of_digits(value)

print(f'{num} -> {sum_total}')
