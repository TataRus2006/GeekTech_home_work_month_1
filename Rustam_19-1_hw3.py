# Счетчик гласных и согласных букв

while True:
    word = input('Введите слово на кирилице или латинице: '.lower())
    vowels = 'аиеёоуыэюяaeiouy'
    consonants = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'
    print(f'Слово: {word}')
    new = 0
    new1 = 0
    new2 = 0
    if word.lower() == 'exit':
        print('Вы произвели выход')
        break

    for i in word.lower():
        if i in vowels or consonants:
            new2 += 1
    print(f'Колличество букв: {new2}')

    for i in word.lower():
        if i in consonants:
            new += 1
    print(f'Согласных букв: {new}')

    for i in word.lower():
        if i in vowels:
            new1 += 1
    print(f'Гласных букв: {new1}')

    percentage_vowel = round(new1 * 100 / new2, 2)
    percentage_of_consonants = round(new * 100 / new2, 2)
    print(f'Гласные/Согласные: {percentage_vowel}% / {percentage_of_consonants}%')

    print()