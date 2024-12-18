array = [7, 8, 6, 1, 9, 1, 2, 9, 4]
elements_dict = {}
for index, value in enumerate(array):
    if value in elements_dict:
        elements_dict[value].append(index)
    else:
        elements_dict[value] = [index]
duplicates_found = False
for value, indices in elements_dict.items():
    if len(indices) > 1:
        print(f"Элемент {value} повторяется на индексах: {indices}")
        duplicates_found = True
if not duplicates_found:
    print("Повторяющихся элементов не найдено.")
