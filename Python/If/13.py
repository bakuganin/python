import random

n = random.randint(1,15)
print("Первое число -",n)
m = random.randint(1,15)
print("Второе число -",m)
x = random.randint(1,15)
print("Третие число -",x)
y = random.randint(1,15)
print("Четвертое число -",y)

d = m*n
print("Метров в бассейне:",d)

mmax = max(n, m)
mmin = min(n, m)
print(mmax,mmin)
n = mmax - y
m = mmin - x
print(min(x,y,m,n))
