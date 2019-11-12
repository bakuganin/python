import random

x1 = random.randint(0,8)
print("Первое число -",x1)
y1 = random.randint(0,8)
print("Второе число -",y1)
x2 = random.randint(0,8)
print("Третье число -",x2)
y2 = random.randint(0,8)
print("Четвертое число -",y2)
#Эта фигура ходит как король, но уже на любое доступное количество клеток,
#ну или,ферзь ходит и как ладья и как слон,
#поэтому можно обьеденить два условия ладьи и слона в одно
if abs(x1-x2) <= 1 and abs(y1-y2) <= 1 or x1 == x2 or y1 == y2:
    print ('YES')
else:
    print ('NO')
