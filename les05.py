date_list = input('Введмите дату:').split('.')

def is_star(list):
    if int(list[0])*int(list[1]) == int(list[2]) % 100:
        return True
    else:
        return

print(is_star(date_list))