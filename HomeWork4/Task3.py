# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randint

number_of_elements = int(input('Введите количество элементов списка: '))

def get_array(number_of_elements):
    array = []
    for i in range(number_of_elements):
        array.append(randint(0, 9))
    return array

def find_non_repeating_elements(arr):
    result = []
    for i in arr:
        if arr.count(i) == 1:
            result.append(i)
    return result

if number_of_elements > 0:
    arr = get_array(number_of_elements)
    print(arr)
    print(find_non_repeating_elements(arr))
else:
    print('Вы ввели некорректное значение элементов')



