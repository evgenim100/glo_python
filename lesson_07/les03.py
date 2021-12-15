print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(b, a+1):
        print(i)
