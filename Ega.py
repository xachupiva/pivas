with open('test') as f:
    count = f.read().count('a')

if count:
    print(f'Количество элементов в файле: {count}')
else:
    print('Элементов в файле нет')
