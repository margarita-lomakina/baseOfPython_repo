while True:
    season_index = int(input('Введите номер месяца (от 1 до 12): '))
    if season_index in range(1, 13):
        break
    else:
        print('Неправильный ввод')

#option1 - dict
season_dict = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for key, value in season_dict.items():
    if season_index in value:
        print('option1 - Сезон:', key)
        break

#option2 - list
season_list = [['зима']*2, ['весна']*3, ['лето']*3, ['осень']*3, ['зима']]
season_list = sum(season_list, [])
print('option2 - Сезон:', season_list[season_index-1])