"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

random_string = ""
for _ in range(random.randint(5, 30)):
    random_string += f"{random.randint(1, 30)} "

with open("test5.txt", "w", encoding="UTF-8") as f_obj:
    print(random_string.rstrip(), file=f_obj, end="")

total = 0
with open("test5.txt", "r", encoding="UTF-8") as f_obj:
    file_arr = f_obj.read().split(" ")
    for i in file_arr:
        total += int(i)
    print(f"Сумма всех чисел в файле: {total}")
