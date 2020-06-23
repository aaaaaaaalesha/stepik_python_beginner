# объявление функции
def is_magic(date):
    s_list = date.split('.')
    return int(s_list[0]) * int(s_list[1]) == int(s_list[2][2:])


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
