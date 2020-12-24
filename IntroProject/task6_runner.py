a = float(input("Введите дистанцию, которцю спортсмен пробегает сейчас: "))
b = float(input("Введите цель спортсмена: "))
day = 1
while True:
    print(f'{day}-й день: {a:.{2}f} км')
    if a >= b:
        break
    else:
        a = 1.1 * a
        day = day + 1
print(f'На {day}-й день спортсмен достиг результата - не менее {b:.{2}f} км')