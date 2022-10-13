name = 'Иван', 'Мария', 'Петр', 'Илья', 'Марина'
temp = ['И', 'М', 'П', 'И', 'М']
list_name = {}
for j in temp:
    for i in name:
        if i[0] in j:
            list_name.setdefault(j, []).append(i)

    # list_name[j] = [i for i in name if i[0] in j]

print(list_name)