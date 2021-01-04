def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    my_sum = max(my_list)
    my_list.remove(my_sum)
    return my_sum + max(my_list)


a, b, c = list(map(int, input("Enter three numbers: ").split()))
print('Sum of two max:', my_func(a, b, c))

