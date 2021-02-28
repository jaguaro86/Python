"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
total = 0
count = 0
with open("test3.txt", "r", encoding="UTF-8") as f_obj:
    for i in f_obj:
        current = i.split(" ")
        if int(current[1]) < 20000:
            print(f"{current[0]} получает меньше 20000")
        total += int(current[1])
        count += 1
    average = total / count
    print(f"Средний доход: {average:.2f}")
