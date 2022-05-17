#Задача 1
for i in range(5):
    print(f'%i 0000' % i)

#Задача 2    
s = 0
for i in range(10):
    n = int(input())
    if (n == 5):
        s += 1
print(s)

#Задача 3
s = 0
for i in range(1, 101):
    s += i 
print(s)

#Задача 4
p = 1
for i in range(2, 11):
    p *= i
print(p)

#Задача 5
n = str(int(input()))
for l in n:
    print(l)
