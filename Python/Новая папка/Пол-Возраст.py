pol = int(input("Какой у тебя пол? *Выбери цифру* - Мальчик(1), Девочка(2)"))
while True:
    if pol == 1:
        age = int(input("Привет, мальчик!) Сколько тебе лет? "))
        if 15<age<19:
            print("Доступ разрешен.")
        else:
            print("Вы не подxодите.")
    elif pol == 2:
        print("Извините этот контент не для девочек((0(")
        break
    else:
        print("такого варианта ответа, нет")
        
    
    
    

