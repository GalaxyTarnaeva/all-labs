colors = ("Синий","Желтый","Красный")
col1 = input("Введите первый цвет: ")
col2 = input("Введите второй цвет: ")
if col1 in colors and col2 in colors:
    if col1 != col2:
        if (col1 in ("Синий","Красный")) and (col2 in ("Синий","Красный")):
            print("Фиолетовый")
        if (col1 in ("Желтый","Красный")) and (col2 in ("Желтый","Красный")):
            print("Оранжевый")
        if (col1 in ("Синий","Желтый")) and (col2 in ("Синий","Желтый")):
            print("Зеленый")
    else:
        print (col1)
else:
    print("Ошибка")