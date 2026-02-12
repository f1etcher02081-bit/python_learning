def printMax(a, b):
    if a > b:
        print(a, 'Максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'Максимально')

printMax(3, 4) #Пряма передача значень

x = 5 
y = 7

printMax(x, y) #Передача змінних в якості аргументів