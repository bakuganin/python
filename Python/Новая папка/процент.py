C = float(input("Введите начальную сумму вклада - "))
n = int(input("Кол-во лет? - "))
p = int(input("Процент? - "))

S = C
for i in range(0,n):
    S = S // 100 * p + S       
print("Количество денег за", n, " лет:", S, "евро")
print("Прибыль:",S - C)
