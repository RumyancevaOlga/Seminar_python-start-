# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

user_number = float(input('Введите число: '))
length_of_user_number = len(str(user_number)) 
our_number = user_number * 10 ** (length_of_user_number - 2)
sum = 0
while our_number > 0:
    sum = sum + our_number % 10
    our_number = our_number // 10
print('Сумма всех цифр числа ', user_number, 'равна', sum)
