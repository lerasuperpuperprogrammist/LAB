price_per_kg = float(input("Введите цену за 1 кг конфет: "))
print("Стоимость конфет:")
for weight in range(1, 11):  
    cost = weight * price_per_kg
    print(f"{weight} кг: {cost:.2f} рублей")
