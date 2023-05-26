import csv
a=0
with open("data.csv", newline='') as file:
    r=csv.DictReader(file,delimiter=";")
    print("Нужно купить:")
    for i in r:
        a+=int(i["Количество"])* int(i["Цена"])
        print(i["Продукт"]+ " -",i["Количество"]+" шт.", i["Цена"]+" руб.")
    print("Итоговая сумма:",a, "руб")