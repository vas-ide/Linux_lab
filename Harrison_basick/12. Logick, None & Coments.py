


age = 35
old = age > 18
print(old)
name = 'Alex'
list_symbol_full = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']

list_symbol_part1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
list_symbol_part2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

second_half = name[0].lower() in list_symbol_part2
print(second_half)

names = ['Alex', 'Leo', 'Ksy', 'Tani']
if names:
    print('Class has enrollments')
else:
    print('The class is empty!')

car = None

if car is None:
    print('Taxi for you!')
else:
    print('You have a car!')