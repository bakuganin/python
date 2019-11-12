import random

x1 = random.randint(0,8)
print("Первое число -",x1)
y1 = random.randint(0,8)
print("Второе число -",y1)
x2 = random.randint(0,8)
print("Третье число -",x2)
y2 = random.randint(0,8)
print("Четвертое число -",y2)

    #конь всегда ходит на 2 клетки по у и по 2 клетки по х
    #если конь идет вниз или вверх то его х изменится на 1 а у на 2
    #если влево или вправо то х на 2 у на 1
    #из этого можно подумать и написать разность
if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print ('YES')
elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
    print ('YES')
else:
    print ('NO')
