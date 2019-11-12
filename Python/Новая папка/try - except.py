try:
    k = 1 / 0
except ZeroDivisionError:
    k = 0
print(k)

f = open('1.txt')
ints = []
try:
    for line in f:
        ints.append(int(line))
except ValueError:
     print('Это не число. Выходим.')
except Exception:
     print('Это что ещё такое?')
else: #Инструкция else выполняется в том случае, если исключения не было.
    print('Всё хорошо.')
finally:
    f.close()
    print('Я закрыл файл.')
# Именно в таком порядке: try, группа except, затем else, и только потом finally.


my_list = [1, 2, 3, 4, 5]
 
try:
    my_list[6]
except IndexError:
    print("Этого индекса нет в списке!")


try:
    1 / 0
except ZeroDivisionError:
    print("Вы не можете делить на 0!")


my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
finally:
    print("The finally statement ran!")

my_dict = {"a":1, "b":2, "c":3}
 
try:
    value = my_dict["a"]
except KeyError:
    print("Произошла ключевая ошибка!")
else:
    print("Ошибка не произошла!")
finally:
    print("В итоге оператор задействован!")
    
try:
    assert False
except AssertionError:
    pass
print('Welcome to Prometheus!!!')


while True:
    x = int(input())

    try:
        result = 1 / x
    except:
        print("Error case")
        exit(0)
    else:
        print("Pass case")
        exit(1)
        

