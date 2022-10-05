# 4.* Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (от 0 до 10) многочлена, записать в файл 
# полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import randint, choice

def get_array(number_of_elements):
    array = []
    for i in range(number_of_elements + 1):
        array.append(randint(0, 9))
    return array

def get_polynomial(arr, number_of_elements):
    items = ['+', '-']
    with open('D:\Домашнее задание GeekBrains\Seminar_python(start)\HomeWork4\Task4.txt', 'a', encoding='utf-8') as my_file:
        for i in arr:
            if i > 0 and number_of_elements > 0:
                my_file.write(f' {i}*x^{number_of_elements} ')
                my_file.write(choice(items))
                number_of_elements -= 1
        if arr[len(arr)-1] != 0:
            my_file.write(f" {arr[len(arr)-1]} = 0 \n")
            my_file.close()

for i in range(3):
    number_of_elements = int(input('Введите число: '))
    if number_of_elements > 0:
        get_polynomial(get_array(number_of_elements), number_of_elements)
