print('Введите символ')
s = input()
if (64 < ord(s) < 91) or (96 < ord(s) < 123):
    print(s.swapcase())