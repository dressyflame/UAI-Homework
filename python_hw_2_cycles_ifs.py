for i in range(5):
    print(f'%i 0000' % i)
    
s = 0
for i in range(10):
    n = int(input())
    if (n == 5):
        s += 1
print(s)

s = 0
for i in range(1, 101):
    s += i 
print(s)

p = 1
for i in range(2, 11):
    p *= i
print(p)

n = str(int(input()))
for l in n:
    print(l)
