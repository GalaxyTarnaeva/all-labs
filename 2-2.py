nom = int(input("Введите номер Вашего места от 1 до 54 :  "))
if nom in range (37,55):
    print("У Вас боковое место")
elif nom % 2 == 0:
    print("У Вас верхнее место")
else:
    print("У Вас нижнее место")
