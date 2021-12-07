#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
gazon = {}

garden_set = set(garden)
meadow_set = set(meadow)

gazon['Garden'] = garden_set
gazon['Meadow'] = meadow_set

pprint(gazon)
# выведите на консоль все виды цветов
# TODO здесь ваш код

print(garden_set | meadow_set)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
print(garden_set & meadow_set)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
print(garden_set - meadow_set)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
print(meadow_set - garden_set)

