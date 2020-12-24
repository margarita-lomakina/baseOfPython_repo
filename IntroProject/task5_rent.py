earnings = int(input("Выручка: "))
expenses = int(input("Издержки: "))
profit = earnings - expenses
if profit >= 0:
    print("Фирма работает с прибылью.")
    print(f"Рентабельность: {(profit/earnings):.{2}f}")
    employees = int(input("Численность работников: "))
    print(f"Прибыль на одного сотрудника: {(profit/employees):.{2}f}")
else:
    print("Фирма работает с убытком.")