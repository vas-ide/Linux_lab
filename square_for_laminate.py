length_room_1 = 410
width_room_1 = 280
s_room_1 = length_room_1 * width_room_1 / 10000

length_room_2 = 410
width_room_2 = 280
s_room_2 = length_room_2 * width_room_2 / 10000

length_main_room_big_sector = 315
width_main_room_big_sector = 305 + 185

length_main_room_smol_sector = 90
width_main_room_smol_sector = 305

s_main_room = ((length_main_room_big_sector * width_main_room_big_sector) +
               (length_main_room_smol_sector * width_main_room_smol_sector)) / 10000
s_all = s_room_1 + s_room_2 + s_main_room

print('Кухня гостиная', s_main_room)
print('Первая комната', s_room_1)
print('Вторая комната', s_room_2)
print('Минимальная общая площадь без дверных проёмов и балкона', s_all)
