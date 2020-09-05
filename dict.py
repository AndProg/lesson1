dict = {'City': 'Москва', 'Temperature': '20'}
print(dict['City'])
print('уменьшенная т-ра:', int(dict['Temperature']) - 5)

dict['Temperature'] = 15

print(dict)

print(dict.get('Country','Россия'))

dict['date'] = '27.05.2019'

print(dict)