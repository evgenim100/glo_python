print('Введите n')
n = int(input())
max = -10**9
min = 10**9
for i in range(0, n):
    num = int(input())
    if max < num:
        max = num
    if min > num:
        min = num
print('Минимум равен', min)
print('Максимум равен', max)