rate_list = [7, 5, 3, 3, 1]
print('Ваш рейтинг: ', rate_list)
flag = 'add'
while flag == 'add':
    new_mark = int(input('Введите новую оценку: '))
    for ind, rate in enumerate(rate_list):
        if new_mark <= rate_list[-1]:
            rate_list.append(new_mark)
            break
        if rate < new_mark:
            rate_list.insert(ind, new_mark)
            break
    print('Ваш новый рейтинг: ', rate_list)
    flag = input('Если вы хотите ввести ещё одну оценку введите add или нажмите enter, чтобы завершить ввод: ')
print('До свидания!')