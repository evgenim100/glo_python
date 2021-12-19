print('Введите n')
count = 0
n = int(input())
for i in range(2, n // 2):
    print(i)
    if n % i == 0:
        print('NO')
        count += 1
        break
if count == 0:
    print('YES')

