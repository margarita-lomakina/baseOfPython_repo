#специальный символ '*'
def sum_line(nums_str):
    return sum(list(map(int, nums_str.split())))


summa = 0
while True:
    line = input('Введите числа через пробел.\nЧтобы завершить суммирование введите "*".\n')
    ind_end = line.find('*')
    if ind_end > 0:
        line = line[:ind_end]
        summa += sum_line(line)
        print('Итоговая сумма:', summa)
        break
    summa += sum_line(line)
    print('Сумма:', summa)

