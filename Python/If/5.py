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
