from math import factorial


def fact(n):
    for i in range(1, n+1):
        yield factorial(i)


number = int(input('Введите число: '))
for el in fact(number):
    print(el)

