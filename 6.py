a = int(input("Количество километров в перый день: "))
b = int(input("Необходимое количество километров: "))
km = a
count = 1

count_mes = f"{count} день: {km:.2f} км;"
print(count_mes)

while km < b:
    km += km/10
    count += 1
    count_mes = f"{count} день: {km:.2f} км;"
    print(count_mes)

final_mes = f"На {count} день спортсмен достигнет результата - не менее {b} км."
print(final_mes)