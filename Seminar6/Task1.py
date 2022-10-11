actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

my_expression = '4 * ( 3 - 1 ) / ( 9 - 7 )'

def remove_brackets(line):
    lst = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            n = line.index(')', i)
            lst.append(line[i + 1:n])
            i = n
        else:
            lst.append(line[i])
        i += 1
    return lst

# print(remove_brackets(my_expression.split()))

def in_brackets(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            a, b, c = remove_brackets(lst[i])
            lst[i] = actions[b](a, c)
    return lst

print(in_brackets(remove_brackets(my_expression.split())))

def result(lst):
    priority = [i for i, j in enumerate(lst) if j in '*/']
    while priority:
        t = priority[0]
        a, b, c = lst[t - 1: t + 2]
        lst.insert(t - 1, actions[b](a, c))
        del lst[t: t + 3]
        priority = [i for i, j in enumerate(lst) if j in '*/']
    
    while len(lst) > 1:
        a, b, c = lst[ :3]
        del lst[ :3]
        lst.insert(0, actions[b](a, c))
    return lst

print(result(in_brackets(remove_brackets(my_expression.split()))))