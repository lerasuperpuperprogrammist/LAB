def geometric_progression(a, r, n):
    return a if n == 1 else r * geometric_progression(a, r, n - 1)
a = float(input("первый член прогрессии a: "))
r = float(input("знаменатель прогрессии r: "))
n = int(input("номер члена прогрессии n: "))
print(f"{n}-й член геометрической прогрессии: {geometric_progression(a, r, n)}")