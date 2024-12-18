k = int(input("Введите значение k: "))
for num in range(1, k + 1):
    n = len(str(num))  
    if num == sum(int(digit)**n for digit in str(num)):
        print(num)
        # armstrong 153=1^3+5^3+3^3