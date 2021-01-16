num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('numbers.txt', encoding='utf-8') as eng_file:
    with open('numbers_rus.txt', 'w', encoding='utf-8') as rus_file:
        for eng_line in eng_file:
            eng_line = eng_line.split()
            eng_line[0] = num_dict[eng_line[0]]
            rus_file.write(' '.join(eng_line) + '\n')

