number = int(input('Введмите номер месяца:'))

def days(n):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(months[n-1])

days(number)