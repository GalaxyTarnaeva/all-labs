n = int(input("задайте количество слов: "))
A = [0]*n
for i in range (0, n):
    print ("Введите слово: ")
    A[i] = input()
    i += 1
for i in range (0, n):
    print (A[i], end = ' ')
    i += 1

