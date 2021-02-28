"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую
файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
rus = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять"]
new_string = ""

with open("test4_1.txt", "r", encoding="UTF-8") as f_obj:
    for i in f_obj:
        current = i.split(" — ")
        position = int(current[1])
        new_string += f"{rus[position]} — {position}\n"

with open("test4_2.txt", "w", encoding="UTF-8") as f_obj:
    print(new_string, file=f_obj)
