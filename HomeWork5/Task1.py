# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

import random

user_number = int(input('Введите количество слов: '))

def get_offer(user_number):
    word = 'абв'
    result = []
    for i in range(user_number):
        temp = random.sample(word, k = 3)
        result.append(''.join(temp))
    my_list = ' '.join(result)
    return my_list

def clean_list(arr):
    word = 'абв'
    arr = arr.split(' ')
    for i in arr:
        if word in arr:
            arr.remove(word)
    my_list = ' '.join(arr)
    return my_list

my_list = get_offer(user_number)
print(my_list)
print(clean_list(my_list))

