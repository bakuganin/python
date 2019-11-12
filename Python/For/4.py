import random
t = 0
x = 0
for i in range(10):
    x = random.randint(1,999)
    print("Число -",x)
    t += x
print("Cумма всех чисел -",t)
