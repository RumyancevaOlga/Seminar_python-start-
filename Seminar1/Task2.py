#a = int(input('a = '))
#b = int(input('b = '))
#c = int(input('c = '))
#d = int(input('d = '))
#e = int(input('e = '))
#max = a
#if(b > max):
#    max = b
#elif(c > max):
#    max = c
#elif(d > max):
#    max = d
#elif(e > max):
#    max = e
#print('max = ', max)

max = 0
for i in range(5):
    n = int(input('Введите число: '))
    if n > max:
        max = n
print('max = ', max)


