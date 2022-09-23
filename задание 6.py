import math

a = (1, 2, 5, 7, 8)
min = 100000000
c = 0
min = 100000000000000
min1 = int(min)
n = len(a)
for i in range(n):
    x = a[i]
    x1 = int(x)
    if x1 % 2 == 0 and min1 > x1:
        min1 = x1
        c = 1
if c == 0:
    print(a[0])
else:
    print(min1)
