import json

firm_dict = {}
avg = 0
firm_count = 0
with open('firm.txt') as f_obj:
    for info_line in f_obj:
        info_line = info_line.split()
        profit = int(info_line[2]) - int(info_line[3])
        firm_dict[info_line[0]] = profit
        if profit >= 0:
            avg += profit
            firm_count += 1

final_list = [firm_dict, {'average_profit': avg/firm_count}]
print(final_list)

with open("firm.json", "w") as write_f:
    json.dump(final_list, write_f)

