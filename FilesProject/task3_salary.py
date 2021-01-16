print('Сотрудники с окладом меньше 20 000:')

with open("task3_salary.txt", "r", encoding='utf-8') as f_obj:
    avg_salary = 0
    employees = 0
    for line in f_obj:
        surname, salary = line.split()
        employees += 1
        salary = float(salary)
        avg_salary += salary

        if salary < 20000:
            print(surname)

print(f'\nСредний оклад по всем сотрудникам: {avg_salary/employees:.2f}')

