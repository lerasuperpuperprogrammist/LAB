import json
def read_json (file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
def filter_users_by_name(data, prefix):
    return [user for user in data if user['name'].startswith(prefix)]
def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
input_file = '/Users/valeriaklimenko/Documents/Lab07/lab.json'
output_file = '/Users/valeriaklimenko/Documents/Lab07/output.json'
users_data = read_json(input_file)
prefix = "Ade"  
filtered_users = filter_users_by_name(users_data, prefix)
write_json(output_file, filtered_users)
print(f"новые данные сохранены в файл {output_file}")