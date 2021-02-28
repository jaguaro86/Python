"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json


average_profit = 0
count_firms = 0
firms = {}
profits = {}
with open("test7.txt", "r", encoding="UTF-8") as f_obj:
    for i in f_obj:
        c_firm = i.split()
        c_profit = int(c_firm[2]) - int(c_firm[3])
        if c_profit > 0:
            average_profit += c_profit
        firms[c_firm[0]] = c_profit
        count_firms += 1
    profits["average_profit"] = average_profit / count_firms
    json_list = [firms, profits]
    print(json_list)

with open("json_example.json", "w") as json_obj:
    json.dump(json_list, json_obj)
