import pickle
students = {
    "Иванов": {"Математика": 8, "Физика": 7, "Информатика": 9, "Маркетинг": 5, "Политология": 7},
    "Мышкин": {"Математика": 6, "Физика": 4, "Информатика": 2, "Маркетинг": 8, "Политология": 7},
    "Баранов": {"Математика": 7, "Физика": 7, "Информатика": 9, "Маркетинг": 6, "Политология": 7},
    "Зуенок": {"Математика": 9, "Физика": 8, "Информатика": 7, "Маркетинг": 8, "Политология": 9},
    "Смирнов": {"Математика": 10, "Физика": 9, "Информатика": 8, "Маркетинг": 7, "Политология": 9},
    "Царев": {"Математика": 4, "Физика": 4, "Информатика": 5, "Маркетинг": 6, "Политология": 7},
    "Пятибратов": {"Математика": 10, "Физика": 10, "Информатика": 10, "Маркетинг": 10, "Политология": 9},
}
print("Список студентов и их баллы:")
for student, scores in students.items():
    print(f"{student}: {scores}")
average_scores = {}
for student, scores in students.items():
    average_scores[student] = sum(scores.values()) / len(scores)

print("\nСредние баллы студентов:")
for student, avg_score in average_scores.items():
    print(f"{student}: {avg_score:.2f}")
max_avg_student = max(average_scores, key=average_scores.get)
min_avg_student = min(average_scores, key=average_scores.get)

print(f"\nСтудент с максимальным средним баллом: {max_avg_student} ({average_scores[max_avg_student]:.2f})")
print(f"Студент с минимальным средним баллом: {min_avg_student} ({average_scores[min_avg_student]:.2f})")
above_avg_math_students = [
    student for student, scores in students.items() if 5 < scores["Математика"] 
]
print(f"\nСтуденты с оценкой выше средней по математике:")
print(", ".join(above_avg_math_students))
with open("data.pickle", "wb") as file:
    pickle.dump(students, file)
with open("data.pickle", "rb") as file:
    loaded_students = pickle.load(file)
print("\nЗагруженные данные из файла:")
print(loaded_students)