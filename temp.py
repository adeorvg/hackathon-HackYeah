import json

data = {'Analiza Matematyczna': {'Całki Oznaczone': (0, 120), 'Rachunek Różniczkowy': (1, 150)},
        'Podstawy Informatyki': {'Maszyna Turinga': (0, 60), 'Synchronizacja Wątków': (1, 150)}}

with open('data.json', 'w') as fp:
    json.dump(data, fp)
    
with open('data.json', 'r') as fp:
    data2 = json.load(fp)
    
for i in data2.keys():
    print(i)
    print('='*50)