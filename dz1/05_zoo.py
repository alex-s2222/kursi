#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
zoo += birds
print(zoo)

#  и выведите список на консоль !выше!


# уберите слона
#  и выведите список на консоль
del zoo[3]
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту
sitLion = zoo.index('lion')+1
print('В', sitLion, 'клетке сидит лев')

sitLark = zoo.index('lark') + 1
print('В', sitLark, 'клетке сидит жаворонок ')

