import csv
def read_and_print_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(" | ".join(f"{key} → {value}" for key, value in row.items()))
def get_min_value(file_path, column):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return min(float(row[column]) for row in reader if row[column])
def get_max_value(file_path, column):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return max(float(row[column]) for row in reader if row[column])
def get_sum_values(file_path, column):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return sum(float(row[column]) for row in reader if row[column])
def get_avg_value(file_path, column):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        values = [float(row[column]) for row in reader if row[column]]
        return sum(values) / len(values) if values else 0
file_path = '13.csv'
print("Содержимое файла:")
read_and_print_csv(file_path)
