from itertools import count, cycle

#A
start = int(input("С какого числа запустим итератор?\n"))
for el in count(start):
    if el - start > 100:
        break
    else:
        print(el)

#B
el_list = ['так', 'все', 'говорят', 'а', 'ты', 'купи', 'слона']
iter = cycle(el_list)

for i in range(20):
    print(next(iter))

i_count = 0
for el in iter:
    if i_count > 20:
        break
    else:
        print(el)
        i_count += 1