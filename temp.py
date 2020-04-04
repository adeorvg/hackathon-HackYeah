import json

data = {'Analiza Matematyczna': {'Całki Oznaczone': (120, 0), 'Rachunek Różniczkowy': (150, 1)},
        'Podstawy Informatyki': {'Maszyna Turinga': (60, 0), 'Synchronizacja Wątków': (150, 1)}}

with open('data.json', 'w') as fp:
    json.dump(data, fp)
    
with open('data.json', 'r') as fp:
    data2 = json.load(fp)
    
for i in data2.keys():
    print(i)
    print('='*50)