#зп без налога брутто, с налогом нетто
adult = input("Введите сколько взрослых: ")
children = input("Введите кол-во детей: ")
y = int(children)
x = int(adult)
zpA = 5000
print()
print("Средний доход одного человека в Эстонии:",zpA)
print()
zpC1 = 60
zpC2 = 100
socnal = 0.33
podoxod = 0.106
bezrab = 0.02
nakopPensia = 0.02
nal = 0
zarplata = 0

nal = float((zpA * podoxod) + (zpA * nakopPensia) + (zpA * bezrab))
nalog = float(zpA - nal)
he = (zpA - nal)


if zpA >= 25200:
    pod


print("Cоц.налог (Платит работадатель -)",zpA*socnal)
print()
print("Подоходный налог -",zpA*podoxod)
print()
print("Накопительная пенсия налог -",zpA*nakopPensia)
print()
print("Налог по страхованию от безработицы",zpA*bezrab)
print()
print("Налог -",nal,"Нетто -", he,", у одного взрослого.")
print()
while True:
    if y >= 3:
        y = y*100
    else:
        y = y*60
    x = x*he
    zarplata = y+x
    break

print("Нетто - Зарплата всех членов семьи за месяц:",zarplata)
print()
print("Нетто - Зарплата всех членов семьи за год:",zarplata*12)
