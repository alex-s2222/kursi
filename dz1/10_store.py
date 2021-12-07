#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# Стол
stoll_code = goods['Стол']
stoll_item = store[stoll_code][0]
stoll_quantity = stoll_item['quantity']
stoll_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
print('Стол-', stoll_quantity, 'стоимость', stoll_cost)

# Диван
divan_code = goods['Диван']
divan_item = store[divan_code][0]
divan_item_1 = store[divan_code][1]
divan_quantity = divan_item['quantity']
divan_quantity_1 = divan_item_1['quantity']
divan_price = divan_item['price']
divan_price_1 = divan_item_1['price']
divan_cost = divan_quantity * divan_price
divan_cost_1 = divan_quantity_1 * divan_price_1
print('Диван1 -', divan_quantity, 'шт, стоимость', divan_cost)
print('Диван2 -', divan_quantity_1, 'шт, стоимость', divan_cost_1)

# Стул1
stul_code = goods['Стул']
stul_item = store[stul_code][0]
stul_quantity = stul_item['quantity']
stul_price = stul_item['price']
stul_cost = stul_quantity * stul_price
print('Стул1-', stul_quantity, 'шт, стоимость', stul_cost)

stul_item_1 = store[stul_code][1]
stul_quantity_1 = stul_item_1['quantity']
stul_const_1 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
print('Стул2-', stul_quantity_1, 'шт стоимость', stul_const_1)

stul_item_2 = store[stul_code][2]
stul_quantity_2 = stul_item_2['quantity']
stul_price_2 = stul_item_2['price']
stul_const_2 = stul_quantity_2 * stul_price_2
print('Стул2-', stul_quantity_2, 'шт стоимость', stul_const_2)
