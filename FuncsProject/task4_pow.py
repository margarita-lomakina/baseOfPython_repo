def my_func(x, y):
    return x**y


def my_func_pow(x, y):
    p = x
    for i in range(-y - 1):
        p *= x
    return 1/p


number, power = input('Введите число и отрицательную степень: ').split()
number = float(number)
power = int(power)
print('Option #1:', my_func(number, power))
print('Option #2:', my_func_pow(number, power))
