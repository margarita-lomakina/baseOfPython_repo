number = int(input("Введите натуральное число"))
max_digit = 0
while number>0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number = number // 10
print(f'Максимальная цифра {max_digit}')