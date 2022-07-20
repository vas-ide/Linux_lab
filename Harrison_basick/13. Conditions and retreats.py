
#________________________________________________________

year = 4001

if year % 4 == 0:
    print(year, 'високосный')
elif year % 100 == 0 and year % 400 == 0:
    print(year, 'високосный')
else:
    print(year, 'не високосный')

list_year = [1600, 1700, 1800, 1900, 1903, 2000, 2002]
for _ in list_year:
    if _ % 4 == 0:
        print(_, 'високосный')
    elif _ % 100 == 0 and _ % 400 == 0:
        print(_, 'високосный')
    else:
        print(_, 'не високосный')

#________________________________________________________

number = 200
if number % 2 == 0:
    print(f'Honest number')
else:
    print(f"Odd number")

number_list = [12, 122, 1222, 11, 111, 111, 1111, 145, 1456]
for number in number_list:
    if number % 2 == 0:
        print(f'Honest number')
    else:
        print(f"Odd number")

#________________________________________________________






