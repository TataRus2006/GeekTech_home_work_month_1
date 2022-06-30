# Пользователь загадывает число до 100, программа должна угадать это число за минимальное количество попыток.
min_number = 1
max_number = 100
attempts = []
while True:
    meaning = (min_number+max_number)//2
    vvod = input(f'Ваше число:{meaning}?(да, >, <)')
    attempts.append(meaning)
    if vvod.lower() == 'да':
        print(f'колличество попыток {len(attempts)}, попытки {attempts}  и загаданное число {meaning}')
        break
    elif vvod == '>':
        min_number = meaning + 1
    elif vvod == '<':
        max_number = meaning - 1
    else:
        print('Введите в программе «да, > или <»')
        continue
with open('results.txt', 'a', encoding='UTF-8' ) as file:
    file.write(f'колличество_попыток= {len(attempts)}, попытки= {attempts}, загаданное_число= {meaning}\n')