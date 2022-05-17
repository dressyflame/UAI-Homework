#Задача 6
n = str(int(input()))
s = 0
for i in n:
    s += int(i)
print(s)

#Задача 7    
n = str(int(input()))
p = 1
for i in n:
    s *= int(i)
print(s)

#Задача 8
n = str(int(input()))
s = 0
for i in n:
    if (i == '5'):
        s += 1
if (s > 0):
    print('Цифра 5 есть в числе')
else:
    print('Цифры 5 нет в числе')

#Задача 9
n = str(int(input()))
s = n[0]
for i in n:
    if (int(s) < int(i)):
        s = i
print(f'Цифра {s} максимальная в числе {n}')

#Задача 10
n = str(int(input()))
s = 0
for i in n:
    if (i == '5'):
        s += 1
print(f'В числе %i 5-ки' % s)
