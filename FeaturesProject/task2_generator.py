init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(init_list[1:]) if el > init_list[i]]
print(f"Исходный список: {init_list}")
print(f"Новый список: {new_list}")

