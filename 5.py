proceeds = int(input("Выручка компании: "))
costs = int(input("Издержки компании: "))

if proceeds > costs:
    print("Компания прибыльная.")
    profit = proceeds - costs
    profitability = (profit / proceeds * 100)
    prof_mes = f"Рентабельность компании {profitability:.2f}%"
    print(prof_mes)
    workers = int(input("Количество сотрудников: "))
    pay = profit/workers
    pay_mes = f"Прибыль на каждого сотрудника: {pay:.2f} денежных единиц."
    print(pay_mes)
elif proceeds == costs:
    print("Компания отработала в ноль.")
else:
    print("Компания убыточная. Расходимся.")