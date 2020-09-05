list1 = [3,5,7,9,10.5]
print('список версия1: ' + str(list1))

list1.append('Python')
print('список версия2: ' + str(list1))

print('первый элемент списка: ' + str(list1[0]))
print('последний элемент списка: ' + str(list1[-1]))
print('элементы списка от 2 до 4: ' + str(list1[0:5]))

list1.remove('Python')
print('список без Python: ' + str(list1))