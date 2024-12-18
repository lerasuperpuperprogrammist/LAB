array = [1, 21, 15, 3, 16, 4, 21, 14]
for i in range(len(array)):
    if array[i] < 15:
        array[i] = array[i] * 2
print("Преобразованный массив:", array)