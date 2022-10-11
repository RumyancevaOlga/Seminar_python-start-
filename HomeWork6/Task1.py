# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

user_number = int(input('Введите количество элементов списка: '))

def f(x):
    x = randint(1, 30)
    return x

my_list = [f(i) for i in range(user_number)]
print(my_list)

new_list = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i] < my_list[i + 1]]
print(new_list)