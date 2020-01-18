import random
print('---------Правила Игры---------')
print('1.Загадайте число от 1 до 100')
print('2.Помогайте боту угадывать число, вводя знаки больше(>) или меньше(<)')
print('3.Если бот угадал число, введите знак "="')
print('------------------------------')

input_key = None
r_num = random.randint(1, 100)
max_num = 100
min_num = 1
tries = 0

while input_key != '=':
    print(f'Вы загадали {r_num}?')
    input_key = input('Введите знак: ')
    if input_key == '>':
        tries += 1
        if min_num < r_num:
            min_num = r_num
            print('Min - ', min_num)
            print('Max - ', max_num)
            r_num = random.randint(min_num+1, max_num-1)
        else:
            print('Min - ', min_num)
            print('Max - ', max_num)
            r_num = random.randint(min_num+1, max_num-1)
    elif input_key == '<':
        tries += 1
        if max_num > r_num:
            max_num = r_num
            print('Min - ', min_num)
            print('Max - ', max_num)
            r_num = random.randint(min_num+1, max_num-1)
        else:
            print('Min - ', min_num)
            print('Max - ', max_num)
            r_num = random.randint(min_num+1, max_num-1)

else:
    print(f'Ура! Я победил! Мне понадобилось {tries} попытки')