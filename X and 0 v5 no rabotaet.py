from os import system
from random import choice

# глобальные константы
EMPTY = '.'
PLAYER_1 = 'X'
PLAYER_2 = '0'


def get_field() -> list[str]:
    ''' Возвращает поле из 9 пустых клеток '''
    field = []
    for i in range(9):
        field.append(EMPTY)
    return field


def draw_field(field: list) -> None:
    ''' Выводит на экран игровое поле по 3 клетки в ряд '''
    system('cls')
    for i in range(0, 9, 3):
        print(field[i], field[i + 1], field[i + 2])


def make_move_computer(field: list, player: str, is_auto: bool, is_center: bool, is_corner: bool):
        '''
        + собрать пустые клетки в список
        выбрать случайный индекс из этого списка
        в клетку по этому индексу поставить туда игрока
        '''
        empty_cells_index = []
        for index in range(9):
            if field[index] == EMPTY:
                empty_cells_index.append(index)
        if is_center:
            if 4 in empty_cells_index:
                field[4] = player 
                return
        random_index = choice(empty_cells_index)
        field[random_index] = player



def make_move_human(field: list, player: str) -> None:
    '''
    Спрашивает у игрока номер клетки поля
    Проверяет, что клетка с таким номером в пределах поля
    Проверяет, занята ли клетка
    При удачных проверках
    Изменяет клетку под выбранным номером на player - символ игрока
    '''
    while True:
        try:
            cell_num = int(input(f'Введите номер клетки для хода {player}: '))  # FIXME: принимать только целые числа
        except ValueError:
            print('Ошибка! Номером клетки должно быть целое число!')
            continue
        if cell_num < 1 or cell_num > 9:
            print('Ошибка! Номер клетки должен быть от 1 до 9 вкл!')
        elif field[cell_num - 1] != EMPTY:
            print('Ошибка! Эта клетка занята!')
        else:
            field[cell_num - 1] = player
            break


def make_move_computer(
        field: list, 
        player: str, 
        is_predicting: bool
        ) -> None:
        '''
        + собрать пустые клетки в список
        выбрать случайный индекс из этого списка
        в клетку по этому индексу поставить туда игрока
        '''
        empty_cells_index = []
        for index in range(9):
            if field[index] == EMPTY:
                empty_cells_index.append(index)
        if is_center:
            if 4 in empty_cells_index:
                field[4] = player 
                return
        if is_predicting:
            for index in empty_cells_index: 
                # сделать ход в этот индекс
                field[index] = player
                # если выиграл этим ходом , то закончить эту функцию
                if get_winner(field, player):
                    return
                field[index] = EMPTY:
                    
                # если нет  - отменить ход
        random_index = choice(empty_cells_index)
        field[random_index] = player


def get_winner(field: list, player: str) -> str:
    # горизонтали
    for i in range(0, 7, 3):
        if field[i] == field[i + 1] == field[i + 2] == player:
            return player

    # вертикали
    for i in range(3):
        if field[i] == field[i + 3] == field[i + 6] == player:
            return player

    # горизонтали
    if field[0] == field[4] == field[8] == player:
        return player

    if field[2] == field[4] == field[6] == player:
        return player

    return ''


def play_Game(is_silent: bool) -> str:
    '''
    Создает поле
    Начинает игру с 1-го хода
    Пока не будет победителя или есть свободные клетки,
    игроки ходя по очереди
    '''
    field = get_field()
    moves = 1
    while True:
        if moves > 9:
            winner = 'ничья'
            break
        if not is_silent:
            draw_field(field)

        if moves % 2:
            player = PLAYER_1
            make_move_human(field, player, False , False)
        else:
            player = PLAYER_2
            make_move_computer(field, player, False, True)

        moves += 1
        winner = get_winner(field, player)
        if winner:
            break
    if not is_silent:
        draw_field(field)
        print('Игра окончена, победил', winner)

    return winner


winners = [0, 0, 0] # X O ничья

for i in range(100):
    winner = play_Game(False)
    if winner == PLAYER_1:
        winners[0] += 1
    if winner == PLAYER_1:
        winners[1] += 1
    else:
        winners[2] += 1

print(f'{PLAYER_1} победил {winners[0]} раз')
print(f'{PLAYER_2} победил {winners[1]} раз')
print(f'ничьих {winners[2]} раз')
