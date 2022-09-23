import random
import math

a = 1
b = 3


for i in range(0,500):
    if i % 2 == 0:
        a = a - 1 / b
    else:
        a = a + 1 / b
    b = b + 2


print(a * 4)
