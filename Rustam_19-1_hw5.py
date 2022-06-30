# Создать словарь: ключом будет домен страны, значениями будут цвета флага страны содержащиеся в сэт

country = {
    "kg": {'yellow', 'red'},
    "kz": {'blue', 'gold'},
    "uz": {'blue', 'white', 'green', 'red'},
    "tj": {'red', 'yellow', 'white', 'green'},
    "az": {'blue', 'red', 'green', 'white'},
    "tm": {'green', 'red', 'white',  'yellow'},
}
while True:
    color = input('Введите цвета или exit для выхода: ')
    if color.lower() == 'exit':
        print('Вы произвели выход')
        break
    for key, values in country.items():
        if set(color.split()).issubset(values):
            print(key)
    else:
        print('Такого цвета нет!')
