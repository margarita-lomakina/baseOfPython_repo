from random import randint

with open('task5_numbers.txt', 'w') as f_obj:
    for i in range(10):
        number = randint(0, 30)
        print(number, file=f_obj, end=' ')

with open('task5_numbers.txt', 'r') as f_obj:
    print(f'Сумма всех чисел в файле {f_obj.name}:', sum(list(map(int, f_obj.readline().split()))))

