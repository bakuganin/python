import time
while True:
    print("<===============================================================>")
    #зп без налога брутто, с налогом нетто
    adult = input("Введите сколько взрослых: ")
    time.sleep(0.5)
    children = input("Введите кол-во детей: ")
    y = int(children)
    x = int(adult)
    time.sleep(0.7)
    print("")
    zpA = int(input("Введите вашу среднюю ЗП на одного человека в месяц: "))
    print("")

    zpC1 = 60
    zpC2 = 100
    socnal = 0.33
    podoxod = 0.106
    bezrab = 0.023
    nakopPensia = 0.02
    nal = 0
    zarplata = 0

    nal = float((zpA * podoxod) + (zpA * nakopPensia) + (zpA * bezrab))
    he = (zpA - nal)


    #Расчет не облагаемоего дохода подоходным налогом.
    if zpA >= 2100:
        zpA = zpA
        podoxod = 0.1928
    elif zpA <=1200:
        if zpA >= 501:
            podoxod = 0
            zpA = zpA 
        else:
            zpA = zpA
            podoxod = 0
    elif 1201>=zpA<=2099:
        zpA = zpA
        podoxod = 0.14866666666666666


    nal = float((zpA * podoxod) + (zpA * nakopPensia) + (zpA * bezrab))
    he = (zpA - nal)

    time.sleep(0.6)
    #Вывод налогов.

    print("|--------------------[ИТОГ - один человек]----------------------|")
    print("[Cоц.налог] (Платит работадатель) -",(zpA*socnal)//1)
    time.sleep(0.6)
    print("[Подоходный налог] -",(zpA*podoxod)//1)
    time.sleep(1)
    print("[Накопительная пенсия налог] -",(zpA*nakopPensia)//1)
    time.sleep(0.6)
    print("[Налог по страхованию от безработицы] -",(zpA*bezrab)//1)
    time.sleep(0.8)
    print("\n[НАЛОГ] -",nal//1,", у одного взрослого.","\n[НЕТТО] -", he//1,"зарплата, у одного взрослого.")
    time.sleep(0.6)
    print("")

    #Зарплата всех членов семьи и налог.
    nal = (nal//1)*x
    while True:
        if y >= 3:
            y = y*100
        else:
            y = y*60
        x = x*he
        zarplata = (y+x)//1
        break

    print("|--------------------[ИТОГ - всех человек]----------------------|")
    print("")
    time.sleep(0.9)
    #Вывод зарплаты за месяц и за год всех членов семьи.
    print("[НАЛОГ] - Всех членов семьи:",nal)
    time.sleep(0.6)
    print("[НЕТТО] - Зарплата всех членов семьи за месяц:",zarplata)
    time.sleep(0.7)
    print("[НЕТТО] - Зарплата всех членов семьи за год:",zarplata*12)
    print("<===============================================================>")
    print()
    while True:
        time.sleep(1)
        
        decision = input("Хотите повторить? \n[1] - Да \n[2] - Завершить сеанс.\n")
        if decision == "1":
            print()
            break
            time.sleep(0.7)
        elif decision == "2":
            print()
            time.sleep(0.7)
            input("Нажмите \"ENTER\" чтобы завершить сеанс.")
            quit()
        else:
            print("Ваш ответ не корректен! Пожалуйста выберите цифру.")
            print()
            
        


