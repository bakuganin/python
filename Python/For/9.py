print("Введите сколько введете n-чисел:")
x = int(input())
null = 0
for i in range(0,x):
    print("Введите число:")
    y = int(input())
    if y == 0:
        null += 1
print("Кол-во нулей -",null)
