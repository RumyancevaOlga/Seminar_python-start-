# * 4. Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

N = int(input('Введите N: '))
array = []
for i in range(-N, N + 1):
    array.append(i)
length_of_array = N * 2 + 1
position_one = int(input('Введите позицию первого элемента списка: '))
position_two = int(input('Введите позицию второго элемента списка: '))
if position_one != position_two:
    if position_one < length_of_array and position_two < length_of_array:
        product_of_numbers = array[position_one - 1] * array[position_two - 1]
        print('Произведение элементов списка ', array, 'на позициях', position_one, 'и', position_two, 'равно', product_of_numbers)
    else:
        print('Error. Вы вышли за границы списка!')
else:
    print('Error. Вы ввели две одинаковые позиции элементов списка!')
