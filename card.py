from random import shuffle
import os

'''
Карты:
    имя
    цена
    масть

Колода: всего карт = цены * масти
    в 1 масти: 6, 7, 8, 9, 10, валет, дама, король, туз

Игроки - от 2 штук

Колода перемешивается

Кажому игроку выдается по 2 карты из колоды

Игрок види только свои карты

Задача - цены всех карт игрока = 21

Ход игрока:
    оставить свои карты и больше не набирать
    или взять еще карту (сколько угодно раз)

Все игроки должны закончить ход

Если у игрока сумма цен всех карт > 21, он проиграл
Если у всех игроков проигрыш, то это ничья

Выигрывает тот, у кого больше очков и тот, кто не проиграл
'''


def get_deck() -> list[dict]:
    suits = ['бубны', 'черви', 'пики', 'крести']
    names = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    deck = []

    for suit in suits:
        for name in names:
            if name in ('валет', 'дама', 'король'):
                value = 10
            elif name == 'туз':
                value = 11
            else:
                value = int(name)
            card = {
                'имя': name,
                'цена': value,
                'масть': suit
            }
            deck.append(card)
    return deck

def get_players():
    player_1 = {
        'человек': True,
        'имя': 'вася',
        'карты': [],
        'счет': 10
    }
    player_2 = {
        'человек': True,
        'имя': 'вася',
        'карты': [],
        'счет': 10
    }
    return [player_1, player_2]


def deals_card(num: int) -> None:
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop(-1))


def show_cards() -> None:
    '''
    Выводит на экран карты игрока
    '''
    for player in players:
        while True:
            os.system('cls')
            for card in player:
                print(card['имя'][''])
            player_option = input('Взять карту? y/n: ')
            if player_option == 'y':
                player['карты'].append(deck.pop(-1))
            else:
                break
deals_card(2)
deck = get_deck()
shuffle(deck)
players = get_players()
show_cards()

for player in players:
    total = 0
    for card in player['карты']:
        total += card['цена']
    print(f'player['имя'], total)
