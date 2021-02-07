user_time = int(input("Введи время в секундах: "))

all_minutes = user_time // 60
seconds = str(user_time % 60).zfill(2)
hours = str(all_minutes // 60).zfill(2)
minutes = str(all_minutes % 60).zfill(2)

time = f"{hours}:{minutes}:{seconds}"

print(time)