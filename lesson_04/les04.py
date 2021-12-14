print('Введите рубли');
r = int(input())
print('Введите копейки');
k = int(input())
print('Введите количество мячей');
n = int(input())
price=(r*100+k)*n
print('За', n, 'мячей нужно заплатить', price//100, 'рублей и', price%100, 'копеек' );