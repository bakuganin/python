n = int(input())
x = int((n**(0.5)))
y = False
for i in range(2,x):
    if n%i == 0:
        y = True
if y == True:
    print("Cостaвное")
else:
    print("Простое")
