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
