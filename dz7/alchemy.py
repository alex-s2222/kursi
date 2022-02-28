# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__

# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Земля':
            return 'Лава'
        elif other.name == 'Воздух':
            return 'Молния'
        elif other.name == 'Вода':
            return 'Пар'
        else:
            return None

    def __str__(self):
        return f'{self.name}'


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if other.name == 'Огонь':
            return 'Лава'
        elif other.name == 'Воздух':
            return 'Пыль'
        elif other.name == 'Вода':
            return 'Грязь'
        else:
            return None

    def __str__(self):
        return f'{self.name}'


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Земля':
            return 'Пыль'
        elif other.name == 'Воздух':
            return 'Ураган'
        elif other.name == 'Вода':
            return 'Шторм'
        elif other.name == 'Огонь':
            return 'Молния'
        else:
            return None

    def __str__(self):
        return f'{self.name}'


class Water:
    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if other.name == 'Земля':
            return 'Грязь'
        elif other.name == 'Воздух':
            return 'Шторм'
        else:
            return None

    def __str__(self):
        return f'{self.name}'


print(Fire(), ' + ', Earth(), '=', Fire()+Earth())
print(Fire(), ' + ', Water(), '=', Fire()+Water())
print(Fire(), ' + ', Air(), '=', Fire()+Air())
print(f'{Water()} + {Water()} = {Water()+Water()}')
print(f'{Earth()}  + {Water()} = {Earth()+Water()}')
print(f'{Air()} + {Earth()} = {Earth()+Air()}')


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
