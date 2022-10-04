# 5. ** Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов. 

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

user_number = int(input('Введите число: '))

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n -2)

def negative_fib(array):
    my_list = []
    for i in range(len(array)):  # разворот
        if (len(array) - i - 1) % 2 != 0:
            my_list.append(-array[-i-1])
        else:
            my_list.append(array[-i-1])
    my_list.append(0) # добавляем ноль
    for i in range(len(array)): # добавляем прямой ряд
        my_list.append(array[i])
    return my_list

list = []
for e in range(1, user_number +  1):
    list.append(fib(e))
print(negative_fib(list))
