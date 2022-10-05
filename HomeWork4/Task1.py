# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

from decimal import Decimal, getcontext 

user_number = Decimal(input('Введите вещественное число: '))
accuracy = str(input('Введите требуемую точность в формате "0.001": '))

def round_decimal(user_number, accuracy):
    getcontext().prec = len(accuracy) - 1
    user_number = user_number * (10**len(accuracy)-1) / (10**len(accuracy)-1)
    return user_number

print(round_decimal(user_number, accuracy))
