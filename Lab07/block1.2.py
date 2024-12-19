with open('input.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile:
    for line_number, line in enumerate(infile, start=1):
        word_count = len(line.split())
        outfile.write(f"Строка {line_number}: {word_count} слов\n")
print("Результаты подсчёта записаны в файл output.txt")