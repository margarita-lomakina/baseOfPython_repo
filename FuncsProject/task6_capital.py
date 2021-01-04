def int_func(word):
    return word.capitalize()


print(int_func('hello'))
line = input('Enter string: ')

line_list = list(map(int_func, line.split()))
print('Option #1:', ' '.join(line_list))

print('Option #2:', line.title())

