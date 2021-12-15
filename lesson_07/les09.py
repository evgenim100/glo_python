print('Введите n')
n = int(input())
count = 0;
for i in range(0, n):
    num = int(input())
    if num % 2 != 0:
        count +=1
if count == 0:
    print('NO')
else:
    print('YES')