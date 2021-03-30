"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
arr = ["Первая строка\n", "Вторая\n", "Ещё одна строчка\n", "Четвёртая\n"]

total = 0
counts = {}
with open("test2.txt", "w", encoding="UTF-8") as f_obj:
    for i in arr:
        f_obj.writelines(i)
        counts[total+1] = len(arr[total].split(" "))
        total += 1
    print(f"Всего {total} строки")
    for key in counts:
        print(f"Строка: {key}, слов: {counts[key]}")
