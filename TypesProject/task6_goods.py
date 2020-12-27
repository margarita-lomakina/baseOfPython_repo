goods = [
    (1, {'name':'мобильный телефон', 'cost':20000, 'amount': 4}),
    (2, {'name':'компьютер', 'cost':100000, 'amount': 8})
]

while True:
    action = input('Добавить новый товар - NEW\n'
                   'Посмотреть цену и количество товара - INFO\n'
                   'Посмотреть аналитику - ANALYTICS\n'
                   'Выйти - Q\n').lower()

    if action == 'q':
        print('Да свидания!')
        break
    elif action == 'new':
        name, cost, amount = input('Введите через пробел название товара, цену и количество: ').split()
        new_dict = dict()
        new_dict['name'] = name.lower()
        new_dict['cost'] = int(cost)
        new_dict['amount'] = int(amount)
        goods.append((len(goods) + 1, new_dict))
    elif action == 'info':
        name = input('Введите наименоание товара: ')
        is_exist = False
        for good in goods:
            if good[1]['name'] == name.lower():
                print(f'{name}\nЦена: {good[1]["cost"]}\nКоличество: {good[1]["amount"]}')
                is_exist = True
        if not is_exist:
            print('Нет такого товара')
    elif action == 'analytics':
        analytics_dict = dict()
        features = goods[0][1].keys()
        for feature in features:
            analytics_dict[feature] = set()
        for good in goods:
            for feature in features:
                analytics_dict[feature].add(good[1][feature])
        for feature in features:
            print(f'{feature}: {analytics_dict[feature]}')
