import math
a=int(input())
b=int(input())
for i in range(a,b):
    c=1
    for j in range (2,i):
      if i%j==0:
          c=0
    if c==1:
        print(i)
    else:
        c=0