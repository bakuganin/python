import random

n = random.randint(1,15)
print("Первое число -",n)
m = random.randint(1,15)
print("Второе число -",m)
k = random.randint(1,20)
print("Третье число -",k)

d = m*n
print("Долек шоколада:",d)

if k < d and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")
