#1
print("Введите 2 числа:")
x = int(input())
y = int(input())

if x > y:
    print(x)
else:
    print(y)

#2
print("Введите число:")
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

#3
print("Введите 4 различных числа:")
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print("YES")
else:
    print("NO")

#4
god = int(input())
if (god % 4 == 0) and (god % 100 !=0) and (god % 400 == 0):
    print("YES")
else:
    print("NO")

#5
import random

x = random.randint(0,999)
print("Первое число -",x)
y = random.randint(0,999)
print("Второе число -",y)
z = random.randint(0,999)
print("Третье число -",z)
if x>y and x>z:
    print("Наибольшее число -",x)

elif y>x and y>z:
    print("Наибольшее число -",y)

else:
    print("Наибольшее число -",z)


#6
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

#7
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

#8
import random

x1 = random.randint(0,10)
print("Первое число -",x1)
y1 = random.randint(0,10)
print("Второе число -",y1)
x2 = random.randint(0,10)
print("Третье число -",x2)
y2 = random.randint(0,10)
print("Четвертое число -",y2)

    #король может пойти в любом направление на 1 клетку
    #если разность между х и у будет 1 или -1
    #или разность одной из диагоналей/кординат будет = 0
    #значит король сможет перейти с одной клетки на другую
if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
    print ('YES')
else:
    print ('NO')


#9
import random

x1 = random.randint(0,10)
print("Первое число -",x1)
y1 = random.randint(0,10)
print("Второе число -",y1)
x2 = random.randint(0,10)
print("Третье число -",x2)
y2 = random.randint(0,10)
print("Четвертое число -",y2)
    #слон всегда ходит по х на 5 клеток и у на 5 клеток
    #разность х1 и х2 и у1 и у2 всегда будет равна
if abs(x1 - x2) ==  abs(y1 - y2):
    print('YES')
else:
    print('NO')

#10
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

#11
if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print ('YES')
elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
    print ('YES')
else:
    print ('NO')

#12
import random

n = random.randint(1,15)
print("Первое число -",n)
m = random.randint(1,15)
print("Второе число -",m)
k = random.randint(1,15)
print("Третье число -",k)

d = m*n
print("Долек шоколада:",d)

if k < d and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")

#13
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

#14
import random
life = 0
print("Как тебя зовут?")
name = input()
n = random.randint(1,50)
print("Ну тогда приступим?",name, "угадай число от 1 до 50",", у тебя 6 попыток.")
while life < 6:
    print("Как ты думаешь, какое?") 
    d = input()
    d = int(d)
    life = life+1
    if d < n:
        print("число больше ") 
    if d > n:
        print("число меньше ")
    if d == n:
        break
if d == n:
    lufe = str(life)
    print(name, ",ты угадал число с ",life,"попытки. Ты выйграл.")
if d != n:
    n = str(n)
    print("У тебя не осталось попыток. Я загадал число ",n ,"Ты проиграл.")
