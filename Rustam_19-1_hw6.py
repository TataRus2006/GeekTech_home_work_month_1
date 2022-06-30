movies = {
    "Django unchained": {
        "John": 10,
        "Jack": 9
    },
    "Green mile": {},
    "Schindler's list": {"Harry": 8, "Oliver": 7, "Jack": 10},
    "The shawshank redemption": {"Thomasr": 10, "Jacob": 8, "Alfie": 9, "Riley": 9},
    "Sherlock holmes": {"William": 5, "James": 8, "Amelia": 2},
    "Seven pounds": {"Olivia": 9, "Jessica": 10, "Emily": 8},
    "Акыркы сабак": {}
}

while True:
    start = int(input(' \n'
                      'Введите одну из нескольких команд: \n'
                      '1 добавить фильм \n'
                      '2 добавить рейтинг к фильму  \n'
                      '3 просматреть рейтинги для всех фильмов \n'
                      '0 выход из программы \n'
                      ''))
    if start == 1:
        start1 = input('Введите название фильма: ').capitalize()


        def add_movies(name):
            if start1 not in movies.keys():
                movies[name] = {}
                print(f'Фильм {start1} успешно добавлен!')
            else:
                print(f'Фильм {start1} уже существует!')


        add_movies(start1)
        print(movies.items())

    elif start == 2:
        start2 = input('Введите название фильма к которуму хотите добавить рейтинг: ').capitalize()

        def add_rete(movie):
            if movie not in movies.keys():
                print("Этого фильма не существует!")
            else:
                name = input("Введите ваше имя:").capitalize()
                for i in movies.values():
                    if name in i.keys():
                        print("Это имя уже есть , введите другое !")
                        return
                rate = int(input("Введите рейтинг: "))
                if rate < 0 or rate > 10:
                    print("Рейтинг должен быть от 0-10!")
                else:
                    movies[movie].update({name: rate})
                    print(f"Добавлен рейтинг для: {name} его рейтинг: {rate}")
        add_rete(start2)
    elif start == 3:
        def rate_f(names):
            if len(movies[names]) == 0:
                return True
        def average(names):
            a = 0
            for key2 in movies[names].keys():
                a += movies[names][key2]
            print(f'{names} средняя оценка: {round(a / len(movies[names]),2)}')
        for key in movies.keys():
            if rate_f(key):
                print(f'{key} рейтинг для данного фильма отсутсвует!')
            else:
                average(key)
    elif start == 0:
        print('Выход из программы произведен!')
        break