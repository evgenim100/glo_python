print('Введите положительное или отрицательное число')
n = int(input())
pos = 0
neg = 0
while n != 0:
    if n > 0:
        pos += 1
    if n < 0:
        neg += 1
    n = int(input())
print(pos*neg)

