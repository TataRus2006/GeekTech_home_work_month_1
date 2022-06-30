# Бесконечный цикл, который будет предлагать пользователю несколько команд:

mentors = ["Аблай", "Камиля", "Адахан"]
data = []

while True:
    print()
    print(f'Текущий список менторов: {mentors}')
    start = int(input(' \n'
                      'Введите одну из нескольких команд: \n'
                      '1 добавление имени \n'
                      '2 изменение имени \n'
                      '3 удаление имени \n'
                      '0 выход из программы \n'
                      ''))
    if start == 1:
        data1 = len(mentors)
        data2 = 0
        name = input('Введите имя ментора: ').title()
        if data1 == 5:
            print('Колличество имен менторов не должно превышать 5')
            continue
        if len(name) >= 15:
            print('Колличество букв в имени ментора не должно превышать 15!')
            continue
        mentors.append(name)
    elif start == 2:
        rename1 = input('Введите заменяемое имя ментора: ').title()
        if rename1 not in mentors:
            print('Введенное имя нет в списке')
            continue
        id_rename1 = (mentors.index(rename1))
        rename2 = input('Введите новое имя ментора: ').title()
        if len(rename2) >= 15:
            print('Колличество букв в имени ментора не должно превышать 15!')
            continue
        mentors.remove(rename1)
        mentors.insert(id_rename1, rename2)
        print(f'имя ментора {rename1} изменено на имя {rename2}')
    elif start == 3:
        delete = input('Для удаления введите имя ментора или его индекс: ').title()
        delete.isdigit()
        if delete.isdigit() == False:
            if delete in mentors:
                mentors.remove(delete)
                print(f'Ментор с именем {delete} был удален')
            elif delete not in mentors:
                print(f'Ментор с именем {delete} не существует')
        if delete.isdigit() == True:
            id_delete = int(delete)
            id_delete2 = id_delete
            if id_delete <= 4:
                print(f'Ментор с именем {mentors[id_delete]} и индексом {id_delete} был удален')
            mentors.pop(id_delete)
            if id_delete >= 5:
                print(f'Ментор с индексом {id_delete} не существует')
    elif start == 0:
        tuple1 = tuple(mentors)
        print((f'Текущий кортеж менторов: {tuple1}'))
        break
    else:
        print()
        print("Данная команда отсутствует! Введите команду в цифровом формате 0 1 2 3 ")
