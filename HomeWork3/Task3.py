# 3. Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное.
# Без использования встроенной функции преобразования, без строк.

# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

user_number = int(input('Введите число: '))

def conversion_to_binary(number):
    result = []
    while number > 0: # находим число
        remains = number % 2
        number = number // 2
        result.append(remains)
    for i in range(len(result)//2): # переворот
        temp = result [i]
        result[i] = result[len(result) - i - 1]
        result[len(result) - i - 1] = temp
    return result

binary_number = conversion_to_binary(user_number)
for i in range(len(binary_number)):
    print(binary_number[i], end = '')


