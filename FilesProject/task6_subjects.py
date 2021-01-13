subjects_dict ={}

with open('subjects.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        sub_list = [el for el in line.split()]
        hours = [el.split('(')[0] for el in sub_list[1:]]
        h_sum = 0
        for h in hours:
            if not h == '—':
                h_sum += int(h)
        subjects_dict[sub_list[0]] = h_sum

print(subjects_dict)

