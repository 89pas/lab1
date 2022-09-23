import random

a = [random.randint(0, 100) for i in range(10)]
b = tuple(a)
min = 101
print(b)
for i in range(10):
    if b[i] < min and b[i] % 2 == 0:
        min = b[i]

if min == 101:
    print(b[0])
print(min)
