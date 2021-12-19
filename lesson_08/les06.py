print('Введите последовательность')
n = int(input())
sum = 0
count = 0
while n != 0:
    sum += n
    count += 1
    n = int(input())
print(sum/count)