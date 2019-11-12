print("Кол-во карточек:")
n = int(input())
y = 0
for i in range(1, n + 1):
    y += i

for i in range(n - 1):
    y -= int(input())
print(y)
