'''  Результаты сессии содержат оценки 5 экзаменов по каждой группе.
Определить средний балл для трех групп студентов одного потока и выдать список
групп в порядке убывания среднего балла. Результаты вывести в виде таблицы с заголовком.'''
import random

class Exams:
    def __init__(self, name_of_group):
        self.name_of_group = name_of_group
        self.scores = self.generate_scores()

    def generate_scores(self):
        # Генерируем оценки для 20 студентов
        if self.name_of_group == 'БФЗ-24-1 ':
            return [[5] * 5 for _ in range(20)]  # У группы БФЗ-24-1 бывают только пятерки!!
        else:
            return [[random.randint(2, 4) for _ in range(5)] for _ in range(20)]  # Другие группы получают не больше 4 :)


    # Функция для вычисления среднего балла по каждому студенту в группе
    def average(self):
        scores = sum(sum(student_scores) for student_scores in self.scores)
        return scores / 100 # 20 студентов * 5 экзаменов


name_of_groups = ['БФЗ-24-1 ', 'БМТМ-24-1', 'БЭН-24-1 ']

# Формируем список групп
list_of_groups = [Exams(name_of_group) for name_of_group in name_of_groups]

# Составляем рейтинг при помощи пузырька
for i in range(len(list_of_groups)):
    for j in range(len(list_of_groups) - 1):
        if list_of_groups[j].average() < list_of_groups[j + 1].average():
            list_of_groups[j], list_of_groups[j + 1] = list_of_groups[j + 1], list_of_groups[j]


print('')
print('       Рейтинг групп:')
print("Группа         |","Средний балл")
print('-' * 30)
for group in list_of_groups:
    print(group.name_of_group,'     |',group.average())
