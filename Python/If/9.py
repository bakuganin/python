import random

x1 = random.randint(0,10)
print("Первое число -",x1)
y1 = random.randint(0,10)
print("Второе число -",y1)
x2 = random.randint(0,10)
print("Третье число -",x2)
y2 = random.randint(0,10)
print("Четвертое число -",y2)

if abs(x1 - x2) ==  abs(y1 - y2):
    print('YES')
else:
    print('NO')
