# Программа для определения знаков зодиака, по средствам ввода дня и месяца рождения


# Основное задание
# day = int(input('введите день рождения: '))
# month = int(input('введите месяц рождения: '))

Дополнительное задание
date = input('введите дату рождения в формате 01-01 или 01/01: ')
day = int(date[0:2])
month = int(date[3:5])


if 21 <= day <= 31 and month == 3 or 1 <= day <= 20 and month == 4:
    print('Овен')
elif 21 <= day <= 30 and month == 4 or 1 <= day <= 20 and month == 5:
    print('Телец')
elif 21 <= day <= 31 and month == 5 or 1 <= day <= 20 and month == 6:
    print('Близнецы')
elif 21 <= day <= 30 and month == 6 or 1 <= day <= 22 and month == 7:
    print('Рак')
elif 23 <= day <= 31 and month == 7 or 1 <= day <= 22 and month == 8:
    print('Лев')
elif 23 <= day <= 31 and month == 8 or 1 <= day <= 22 and month == 9:
    print('Дева')
elif 23 <= day <= 30 and month == 9 or 1 <= day <= 22 and month == 10:
    print('Весы')
elif 23 <= day <= 31 and month == 10 or 1 <= day <= 21 and month == 11:
    print('Скорпион')
elif 22 <= day <= 30 and month == 11 or 1 <= day <= 21 and month == 12:
    print('Стрелец')
elif 22 <= day <= 31 and month == 12 or 1 <= day <= 19 and month == 1:
    print('Козерог')
elif 20 <= day <= 31 and month == 1 or 1 <= day <= 18 and month == 2:
    print('Водолей')
elif 19 <= day <= 29 and month == 2 or 1 <= day <= 20 and month == 3:
    print('Рыбы')
else:

    print()
    print("Вводите дату рождения от 1 до 31 в формате 01, тире или слэш \n"
          'затем месяц рождения от 1 до 12 в формате 01.')


