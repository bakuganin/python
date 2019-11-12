import random
n = int(input())
t = 0
x = 0
for i in range(n):
    x = random.randint(1,999)
    print("Число -",x)
    t += x
print("Cумма всех чисел -",t)
