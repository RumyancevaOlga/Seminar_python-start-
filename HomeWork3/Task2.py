# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

number_of_elements = int(input('Введите количество элементов списка: '))

def get_array(number_of_elements):
    array = sample(range(1, 10), number_of_elements)
    return array

def product_of_pair_of_list(array):
    result = []
    if len(array) % 2 == 0: # проверка на количество элементов в массиве (чет или нечет)
        length = len(array)//2
    else:
        length = len(array)//2 + 1
    for i in range(0, length): # нахождение результата
        if i != len(array) - i - 1:
            product = array[i] * array[len(array) - i - 1]
        else:
            product = array[i]
        result.append(product)
    return result

my_array = get_array(number_of_elements)
print(my_array)
print(product_of_pair_of_list(my_array))