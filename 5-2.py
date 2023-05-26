from random import randint
a = []
for i in range(6):
    m = randint(1, 10)
    a.append(m)
b = a.copy()
for i in range (0,6):
    for j in range (i+1,6):
        if a[i]==b[j]:
            print(a[i])
        else:
            j += 1
    i += 1
