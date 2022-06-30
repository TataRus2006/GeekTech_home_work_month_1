# ten = list(range(1, 11))
# evens = list(filter(lambda x: x % 2 == 0, ten))
# evens_squared = list(map(lambda x: x * x, evens))
# print(evens_squared)
#
#
# def show(list=ten):
#     while True:
#         try:
#             command2 = int(input('enter index \n'))
#             if command2 == 77:
#                 print('stop program')
#                 break
#             print(list[command2])
#         except ValueError:
#             print('Буквы не вводить, только числа!')
#         except IndexError:
#             print(f"Вводить только числа от 0 до {len(list) - 1} или 77 выход из программы")
#
#
# show()

ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
evens_squared = list(map(lambda x: x * x, evens))
print(evens_squared)
lst_numbers = (ten, evens, evens_squared)
command1 = int(input('enter list: 0 - "ten", 1 - "evens", 2 "evens_squared" 77 выход из программы \n'))
print(lst_numbers[command1])


def show(list=ten):
    while True:
        try:
            command2 = int(input('enter index \n'))
            if command2 == 77:
                print('stop program')
                break
            print(list[command2])
        except ValueError:
            print('Буквы не вводить, только числа!')
        except IndexError:
            print(f"Вводить только числа от 0 до {len(list) - 1} или 77 выход из программы")


show(lst_numbers[command1])