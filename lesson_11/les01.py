n = int(input('Введите n:'))
strings = []
search = ''
for i in range(n):
    strings.append(input('Введите строку:'))
search = input('Введите поисковую строку:')
for i in range(n):
    low_str = strings[i].lower()
    if low_str.find(search.lower()) != -1:
        print(strings[i])
