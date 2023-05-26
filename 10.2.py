import json
name = input("Название: ")
price = input("Цена: ")
avale = input("Есть в наличии: ")
weight = input("Вес: ")

def change(dat):
    with open("2.json","r+",encoding='utf-8') as file: #открываю файл с возможностью открыть и записать, чтобы русские буквы не сломались
        file_data = json.load(file)  # переменная, которая загружает файл, функция лоэд преобразует объект джейсон в объект питон
        file_data['products'].append(dat)
if avale == "Да":
    avale = True
else:
    avale = False
y = {
    "name": name,
    "price": price,
    "available": avale,
    "weight": weight
    }
change(y)  # запуск функции с помощью У
with open("2.json", encoding='utf-8') as f:
    data = json.load(f)
prod = data['products']
for i in prod:
    print('Название: ' + i["name"])
    print('Цена: ' + str(i["price"]))
    print('Вес: ' + str(i["weight"]))
    if i['available'] == True:
        print('В наличии', "\n")
    else:
        print('Нет в наличии', "\n")