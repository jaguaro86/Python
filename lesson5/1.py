"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open("test1.txt", "a", encoding="UTF-8") as f_obj:
    while True:
        user_input = input("Введите строку: ")
        if user_input == "":
            break
        f_obj.writelines(f"{user_input}\n")
