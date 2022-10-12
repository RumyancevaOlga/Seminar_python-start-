# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия», 
# возвращает словарь, ключи — первые буквы фамилий, значения — словари, 
# реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out

# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 
# 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 
# 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}

my_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев",
"Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
"Борис Аркадьев", "Антон Серов", "Павел Анисимов"]
surname_list = []

for i in range(len(my_list)):
    x = my_list[i].split()
    j = x[1]
    surname_key = j[0]
    surname_list.append((surname_key, my_list[i]))

def my_dict(my_list):
    my_diction = {}
    for i, j in my_list:
        my_diction.setdefault(i, []).append(j)
        sorted(my_diction.items())
    return my_diction

surname_dict = my_dict(surname_list)

for v in surname_dict:
    y = surname_dict[v]
    name_list = []
    for i in range(len(y)):
        z = y[i].split()
        d = z[0]
        name_key = d[0]
        name_list.append((name_key, y[i]))
        name_dict = my_dict(name_list)
    surname_dict[v] = name_dict

print(surname_dict)       


