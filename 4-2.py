def zad2(number):
    rez = None
    try:
        rez = 100 / float(number)
    except ValueError:
        print ("В эту функцию нужно передать число ")
    except ZeroDivisionError:
        print("Деление на ноль невозможно ")
    except Exception as e:
        print("Ошибка ", e)
    return rez
print("Проверка функции: деления 100 на число ")
print(zad2(10))
print(zad2("g"))
print(zad2(0))


