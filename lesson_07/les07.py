print('Введите n')
sum = 1
n = int(input())
for i in range(0, n+1):
    if i % 10 == 2 or i % 10 == 9:
        sum *= i;
if sum == 1:
    print(0)
else:
    print(sum)