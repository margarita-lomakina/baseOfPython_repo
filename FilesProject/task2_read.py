lines_count = 0
word_count = []
try:
    with open('nabokov.txt', encoding='utf-8') as f_obj:
        for line in f_obj:
            lines_count += 1
            word_count.append(len(line.split()))
except IOError:
    print('Произошла ошибка ввода/вывода')

print('Количество строк в файле: ', lines_count)
for i, num in enumerate(word_count):
    print(f'{i}: {num}')

