player = {
    'имя': 'Вася Питонов',
    'жизни': 10,
}
player['опыт'] = '4'
for key, value in player.items():
    print(key, '-', value)
print(player.values())