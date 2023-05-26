from random import randint
a = []
k = 0
for i in range(5):
    m = randint(1,15)
    a.append(m)
p = int(input('Введите число: '))
for i in range(5):
    if p == a[i]:
        k+=1
if k > 0:
    print(a)
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")
