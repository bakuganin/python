print("3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны)")
import random

x = random.randint(0,50)
print("Первое число -",x)
y = random.randint(0,50)
print("Второе число -",y)
z = random.randint(0,50)
print("Третье число -",z)

if x == y and x == z:
    print("3")
elif y == x:
    print("2")
elif z == x:
    print("2")
elif z == y:
    print("2")
else:
    print("0")
