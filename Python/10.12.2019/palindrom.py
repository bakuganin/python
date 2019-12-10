def palindrom():

    text = input("Введите текст: ")
    l = len(text)
    #если буква или число с индексом не симетрчино символу с конца то это не палиндром
    for i in range(l//2):
        if text[i] != text[-1-i]:
            print("Это не палиндром.")
        else:
            print("Это палиндром.")
    
while True:
    palindrom()
    x = input("Хотите повторить? Да - нажмите \"ENTER\" Нет - введите 1 ")
    if x == "1":
        break
    else:
        print()
print()
input("press - ENTER")






def reverse(text):
    return text[::-1]
def is_polindrome(text):
    return text.replace(' ','')==reverse(text).replace('','')

i = 0
while i<3:
    something = input("\nВведите текст: ")
    if (is_polindrome(something)):
        print("Да, слово",something,"палиндром")
    else:
        print("Нет, слово",something,"не палиндром")
    i+=1

