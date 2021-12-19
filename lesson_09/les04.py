print('Введите n')
n = int(input())
for i in range(1, n+1):
    if not (2 <= i <= 8 or 128 <= i <= 256 or 1024 <= i <= 2048):
        print(i)





