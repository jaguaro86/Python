# 1.Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

l1 = [1, "2", (1, 2), [], {}, set(), ZeroDivisionError]

i = 0
while i < len(l1):
    print(type(l1[i]))
    i += 1
