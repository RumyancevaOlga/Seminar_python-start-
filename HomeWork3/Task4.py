# 4.* Задайте список из произвольных вещественных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform # генерация псевдослучайных вещественных чисел

number_of_elements = int(input('Введите количество элементов списка: '))

def get_array(number_of_elements):
    array = []
    for i in range(number_of_elements):
        array.append(round(uniform(0, 20), 2))
    return array

def take_fractional_part(array):
    for i in range(0, len(array)):
        array[i] = round(array[i] - int(array[i]), 2)
    return array

def find_max_and_min(array):
    maximum = 0
    if array[1] > array[0]:
        maximum = 1
        minimum = 0
    else:
        minimum = 1
    if len(array) > 2:
        for i in range (2, len(array)):
            if array[i] > array[maximum]:
                maximum = i
            elif array[i] < array[minimum]:
                minimum = i
    result = [maximum, minimum]
    return result

my_array = get_array(number_of_elements)
print(my_array)
my_array = take_fractional_part(my_array)
print(my_array)
min_max = find_max_and_min(my_array)
print(min_max)
print('Разность между максимальным и минимальным значением дробной части элементов ровна: ', 
round(my_array[min_max[0]] - my_array[min_max[1]], 2))
