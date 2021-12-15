print('Введте первую статью')
first = input()
max = len(first)
article = first;
print('Введте вторую статью')
second = input()
if len(second) > max:
    max = len(second)
    article = second
print('Введте третью статью')
third = input()
if len(third) > max:
    max = len(third)
    article = third
print(article)