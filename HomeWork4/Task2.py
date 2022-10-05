# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

user_number = int(input('Введите число: '))

def find_prime_factors(user_number):
    result = []
    while user_number % 2 == 0 or user_number % 3 == 0 or user_number % 5 == 0:
        if not user_number % 2:
            result.append(2)
            user_number /= 2
        elif not user_number % 3:
            result.append(3)
            user_number /= 3
        elif not user_number % 5:
            result.append(5)
            user_number /= 5
    if user_number > 1:        
        result.append(int(user_number))
    return result

print('Список простых множителей числа ', user_number, ' равен ', find_prime_factors(user_number))


