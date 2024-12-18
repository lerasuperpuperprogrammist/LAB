total_sum = 0 
count = 0   
print("Введите последовательность чисел, заканчивающуюся нулем:")
while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    total_sum += number
    count += 1
print(f"Сумма чисел: {total_sum}")
print(f"Количество чисел: {count}")