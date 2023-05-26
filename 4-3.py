def zad3(date: str):
    try:
        date = date.split(".")
        if int(date[0]) * int(date[1]) == int(date[2][2:]):
            return True
        else:
            return False
    except:
        print("Фунция принимает строку вида dd.mm.yyyy ")
print(zad3("22.01.2022"))
print(zad3("23.05.2004"))
