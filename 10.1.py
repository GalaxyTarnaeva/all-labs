import json #тип данных словари
with open("1.json", encoding='utf-8' ) as f:
    data = json.load(f) #открываем файл
prod=data['products'] #переменная для ключа
for i in prod:
    print('Название: '+ i["name"])
    print('Цена: ' + str(i["price"]))
    print('Вес: ' + str(i["weight"]))
    if i['available']==True:
        print('В наличии', "\n")
    else:
        print('Нет в наличии', "\n")