from collections import Counter

names = [
    'Вася',
    'Ася',
    'Квася',
    'Вася',
    'Вася',
    'Ася',
]

counter = dict(Counter(names))

#for name in names:
    #if name not in counter:
       # counter[name] = 1
    #else:
        #counter[name] += 1
for k, v in counter.items():
    print(f'{k} : {v}')