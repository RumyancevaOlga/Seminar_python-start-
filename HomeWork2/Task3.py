# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и 
# выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input('Введите число: '))
array = []
for i in range(1, n + 1):
    array.append(round(((1 + 1/i) ** i), 0))
sum = 0
for i in range(n):
    sum = sum + array[i]
print('Сумма всех чисел из списка ', array, 'равна', sum)
