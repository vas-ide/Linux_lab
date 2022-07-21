
#1._________________________________________________________________
names_friends_and_colleagues = ['Alex', 'Ksy', 'Andrey', 'Viktor', 'Sergio', 'Leonid', 'Vitaliy', 'Romeo', 'Konstantin',
                                'Leonid', 'Alexandr', 'oleg']
len_all_names = 0
for i in names_friends_and_colleagues:
    len_all_names += len(i)
print(len_all_names / len(names_friends_and_colleagues), 'Round -', round(len_all_names / len(names_friends_and_colleagues)))
#2._________________________________________________________________
for i in names_friends_and_colleagues:
    if i == 'John':
        print('Jon+hn is hear')
else:
    print('I dont have friend John ')
#3._________________________________________________________________
names_friends_and_colleagues_tuple = (['Alex', 'V-----n', 35], ['KSY', 'V-----n', 35], ['Leonid', 'V-----n', 4],
                                      ['Vitaliy', 'Kud', 35], ['Konstantin', 'Shtepa', 28],
                                      ['Leonid', 'Evstegneev', 35], ['Alexandr', 'Instructor', None])
average_age = 0
for i in names_friends_and_colleagues_tuple:
    if i[2] == None:
        continue
    else:
        average_age += int(i[2])
average_age_middle = (average_age / len(names_friends_and_colleagues_tuple))
for i in names_friends_and_colleagues_tuple:
    if i[2] == None:
        print(f'{i[0]} возраст неизвестен')
    elif i[2] > average_age_middle:
        print(f'{i[0]} Old')
    elif i[2] < average_age_middle:
        print((f'{i[0]} Young'))

























