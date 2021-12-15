print('Введите n')
sum = 0
n = int(input())
for i in range(0, n+1):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7:
        sum += i;
print(sum)