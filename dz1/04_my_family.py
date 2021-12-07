#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Отец', 'Мама', 'Бабушка', 'Дедушка']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Михaил', 185],
    ['Елена', 165],
    ['Ольга', 165],
    ['Уонстантин', 175]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
rost_father = my_family_height[0][1]
print('Рост отца= ', rost_father)

rost_mother = my_family_height[1][1]
rost_ba = my_family_height[2][1]
rost_de = my_family_height[3][1]
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

owerallGrowth = (rost_de + rost_ba + rost_mother + rost_father) / 4
print('Общий рост семьи= ', owerallGrowth)

print(len(my_family_height))