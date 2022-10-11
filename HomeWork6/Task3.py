# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 
# 'П': ['Петр', 'Петр']}

name = ''
my_list = []

while name != 'esq':
    name = input('Введите имя сотрудника. Для окончания введите esq. ')
    if name != 'esq':
        my_list.append((name[0], name))
    print(my_list)

def my_dict(my_list):
    my_diction = {}
    for i, j in my_list:
        my_diction.setdefault(i, []).append(j)
    sorted(my_diction.items())
    return my_diction

print(my_dict(my_list))