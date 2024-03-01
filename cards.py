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
        'имя': names,
        'цена': value,
        'масть': suit
    }
    deck.append(card)

print('Всего в колоде:', len(deck))
for card in deck:
    print(card)
    print('-' *45 )
