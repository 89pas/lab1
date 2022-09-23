import math
n = 0
k1 = 0
k2 = 0
str = input(('Введите строку'))
str1 = 'ауеыояиёюэ'
str2 = 'йцкнгшщзхъфвпрлджчсмтьб'
n = len(str)
for i in range(n):
    c = 0
    for j in range(10):
        if str[i] == str1[j]:
            k1 = k1 + 1
            c = 1
    if c == 0:
        for y in range(23):
            if str[i] == str2[y]:
                k2 = k2 + 1

if k1 == k2:
    for i in range(n):
        for j in range(10):
            if str[i] == str1[j]:
                print(str[i])
else:
    print(k1, k2)
