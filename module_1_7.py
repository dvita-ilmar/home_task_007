'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №7
Дополнительное практическое задание по модулю: "Базовые структуры данных."
'''
# Заданы списки оценок
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Задан список студентов
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Зададим пустой слварь для итога
journal_of_final_grades = {}

# Решение
# Вычислим средние баллы
average_score = [] # Пустой список для средних баллов
for i in range(0,len(grades)): # Ну не смог я здесь обойтись без цикла
    average_score.append(sum(grades[i])/len(grades[i]))
# Отсортируем эелементы списка студентов с помощью некоей функции
abc_students = sorted(students)

# Запоняем словарь
journal_of_final_grades = dict(zip(abc_students, average_score))
# Вывод результата
print(journal_of_final_grades)


