from num_engine import put_stone, get_bunches, is_gameover, take_from_bunch



put_stone()
user_number = 1
while True:
    print('Текущая позиция')
    print(get_bunches())
    print('Ход икрока {}'.format(user_number))
    pos = input('Откуда берем?')
    qua = input('Сколько берем?')
    take_from_bunch(position=int(pos), quantity=int(qua))
    if is_gameover():
        break
    user_number = 2 if user_number == 1 else 1

print('Выиграл игрок номер{}'.format(user_number))