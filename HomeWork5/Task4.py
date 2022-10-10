# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

# вариант игрок против игрока
from random import choice

def take_candy(user_name):
    candies = int(input(f'Ход делает {user_name}. Введите количество конфет: '))
    if candies < 1 or candies > 28:
        candies = int(input('Введите корректное значение (от 1 до 28): '))
    return candies

def for_print(user_name, candies, count, num_of_candies):
    print(user_name, ' взял ', candies, ' конфет/ы/у. Теперь у него ', count, ' конфет/а/ы. На столе осталось ', num_of_candies, ' конфет/а.')

def game(lot, num_of_candies):
    count_one = 0
    count_two = 0
    lot_of_lot = choice(lot)
    while num_of_candies > 28:
        if lot_of_lot:
            candies = take_candy(first_user_name)
            count_one += candies
            num_of_candies -= candies
            lot_of_lot = False
            for_print(first_user_name, candies, count_one, num_of_candies)
        else:
            candies = take_candy(second_user_name)
            count_two += candies
            num_of_candies -= candies
            lot_of_lot = True
            for_print(second_user_name, candies, count_two, num_of_candies)
    if lot_of_lot:
        print('Выиграл ', first_user_name, '!')
    else:
        print('Выиграл ', second_user_name, '!')


lot = range(0,2)
first_user_name = input('Введите имя первого игрока: ')
second_user_name = input('Введите имя второго игрока: ')
num_of_candies = 2021

game(lot, num_of_candies)