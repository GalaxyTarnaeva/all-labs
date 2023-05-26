from random import randint
mist=0
right=0
while mist!=3:
    m = randint(1, 10)
    n = randint(1, 10)
    summ=m+n
    print(m,"+",n)
    f=int(input())
    if f == summ:
        print("Правильно!")
        right+=1
    else:
        mist+=1
        print("Ответ неверный")
print("Игра окончена.", "Правильных ответов:", right)
