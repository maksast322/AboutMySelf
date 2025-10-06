minutes = int(input("Введите кол-во минут:"))
hours = minutes // 60
last_minutes = minutes % 60
print(f"{minutes} минут - это {hours} час(ов) и {last_minutes} минут")