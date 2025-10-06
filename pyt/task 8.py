zena = int(input("Введите цену: "))
skidos = int(input("Введите процент скидоса: "))

new_zena = zena * (1 - skidos / 100)
print(f"Цена после скидки: {new_zena}")
samaya_new_zena = zena - 10
print(f"Цена после купона {samaya_new_zena}")