time = int(input('Введите время в секундах'))
seconds = time % 60
time = time // 60
hours = time // 60
minutes = time % 60
print(f'{str(hours).rjust(2, "0")}:{str(minutes).rjust(2, "0")}:{str(seconds).rjust(2, "0")}')