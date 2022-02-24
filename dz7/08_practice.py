# -*- coding: utf-8 -*-
from random import randint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я-{}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 30
        self.fullness -= 10

    def watch_NTV(self):
        print('{} смотрел НТВ целый день'.format(self.name))
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 30:
            print('{} сходил в магазин'.format(self.name))
            self.house.money -= 30
            self.house.food += 30
        else:
            print('{} кончились деньги!'.format(self.name))

    def go_into_to_house(self, house):
        self.house = house
        print('{} вьехал в дом'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} die'.format(self.name))
            return 1
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food <= 30:
            self.shopping()
        elif self.house.money <= 30:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_NTV()


class House:
    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(
            self.food, self.money)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Барт')
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_to_house(house=my_sweet_home)

for day in range(1, 321):
    print('\n================= день {} ============='.format(day))
    for citizen in citizens:
        die = citizen.act()
        if die == 1:
            break
    if die == 1:
        break
    print('================================================')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)


# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
