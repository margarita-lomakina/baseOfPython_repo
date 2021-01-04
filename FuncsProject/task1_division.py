def my_division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "It's impossible to divide by zero"


a, b = list(map(int, input('Введите два числа: ').split()))
print(my_division(a, b))
