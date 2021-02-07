# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_input = str(input("Введите число: "))

num1 = int(user_input)
num2 = int(user_input+user_input)
num3 = int(user_input+user_input+user_input)

print(num1+num2+num3)