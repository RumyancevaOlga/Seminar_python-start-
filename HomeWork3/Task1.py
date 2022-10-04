# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import sample, randint

number_of_elements = int(input('Введите количество элементов списка: '))

def get_array(number_of_elements):
    # array = sample(range(1, 20), number_of_elements)
    array = []
    for i in range(number_of_elements):
        array.append(randint(0, 9))
    return array

def sum_of_odd_elements(array):
    sum = 0
    for i in range(0, len(array), 2): # указываем шаг 2
        sum = sum + array[i]
    return sum

my_array = get_array(number_of_elements)
print(my_array)
print(sum_of_odd_elements(my_array))