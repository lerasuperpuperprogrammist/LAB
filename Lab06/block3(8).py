text = input("Введите строку, заканчивающуюся точкой: ")
text_without_dot = text.rstrip('.')
words = text_without_dot.split()
word_count = len(words)
print(f"Количество слов в строке: {word_count}")