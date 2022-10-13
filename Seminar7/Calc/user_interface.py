import modul_div as div
import modul_mult as mult
import modul_sub as sub
import modul_sum as sum

def button_click():
    print('Какую операцию будем производить?')
    print('1. Сложение')
    print('2. Вычитание')
    print('3. Деление')
    print('4. Умножение')
    operation = int(input())

    if operation == 1:
        a = int(input('Введите первое значение: '))
        b = int(input('Введите второе значение: '))
        result = sum.sum(a, b)
        print('Сумма равна: ', result)

