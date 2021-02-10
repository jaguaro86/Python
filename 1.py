# 1. Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные,
# выведите на экран.

import datetime
now_date = datetime.date.today()
caption = "Сегодня: "
print(caption, now_date)

name = input("Как тебя зовут? ")
surname = input("Какая у тебя фамилия? ")
yo = int(input("В каком году ты родился? "))
age = int(now_date.year)-yo

mess = f"{name} {surname}, тебе примерно {age} лет!"

print(mess)