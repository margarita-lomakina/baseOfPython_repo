with open("task1_text.txt", "w") as f_obj:
    while True:
        new_line = input()
        if not new_line:
            break
        else:
            f_obj.write(new_line + '\n')

