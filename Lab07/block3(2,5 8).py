import os
import shutil

def show_file_content(file_path):

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            print(file.read())
    else:
        print(f"Файл {file_path} не найден.")

def create_file_or_folder(path):
    if os.path.exists(path):
        print(f"Путь {path} уже существует.")
    elif path.endswith(os.sep):
        os.makedirs(path)
        print(f"Папка {path} создана.")
    else:
        with open(path, 'w', encoding='utf-8') as file:
            pass
        print(f"Файл {path} создан.")

def copy_file_or_folder(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"файл или папка {src_path} не найден.")
        return

    if os.path.isdir(src_path):
        shutil.copytree(src_path, dest_path)
        print(f"Папка {src_path} скопирована в {dest_path}.")
    elif os.path.isfile(src_path):
        shutil.copy2(src_path, dest_path)
        print(f"Файл {src_path} скопирован в {dest_path}.")
        # print("File", src_path, "Copied in", dest_path)
    else:
        print(f"Неизвестный тип пути: {src_path}.")

if __name__ == "__main__":
    while True:
        print("\nФайловый менеджер:")
        print("1. Показать содержимое файла")
        print("2. Создать файл/папку")
        print("3. Копировать файл/папку")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            file_path = input("Введите путь к файлу: ")
            show_file_content(file_path)
        elif choice == "2":
            path = input("Введите путь для создания файла/папки: ")
            create_file_or_folder(path)
        elif choice == "3":
            src_path = input("Введите путь источника: ")
            dest_path = input("Введите путь назначения: ")
            copy_file_or_folder(src_path, dest_path)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
