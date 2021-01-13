from sys import argv

script_name, hours, wage_rate, bonus = argv

print("Your salary: ", (int(hours) * int(wage_rate)) + int(bonus))

