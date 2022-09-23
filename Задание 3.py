list = [1.34, 'qwerty', 12, 13, 16, 'Love', 'Python']
print(list)
numbers = []
words = []
numb = '1234567890'
n = len(list)
for i in range(n):
    x = list[i]
    c = 0
    s = str(x)
    fnumb = s[0]
    for j in range(10):
        if numb[j] == fnumb and c == 0:
            numbers.append(s)
            c = 1
        if c == 0:
            words.append(s)
            c = 1
print(numbers)
print(words)
n1 = len(numbers)
sum = 0
proizved = 1

for i in range(n1):
    numbe = float(numbers[i])
    sum = sum + numbe
    proizved = proizved * numbe
print('сумма = ', sum)
print('Произведение = ', proizved)
for i in range(3):
    maxel = max(numbers)
    print(maxel)
    numbers.remove(maxel)
