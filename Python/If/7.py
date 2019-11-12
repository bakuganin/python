import random

x1 = random.randint(0,50)
print("Первое число -",x1)
y1 = random.randint(0,50)
print("Второе число -",y1)
x2 = random.randint(0,50)
print("Третье число -",x2)
y2 = random.randint(0,50)
print("Четвертое число -",y2)

# когда ладья ходит, координата по одной из осей не меняется
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
