print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
for i in range(a, b+1):
    if i % 2 == 0:
        print(i)