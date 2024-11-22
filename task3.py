'''  Результаты сессии содержат оценки 5 экзаменов по каждой группе.
Определить средний балл для трех групп студентов одного потока и выдать список
групп в порядке убывания среднего балла. Результаты вывести в виде таблицы с заголовком.'''
import random

class Exams:
    def __init__(self, name_of_group):
        self.name_of_group = name_of_group
        if self.name_of_group == 'БФЗ-24-1':
            for _ in range(20):
                self.one = 5
                self.two = 5
                self.three = 5
                self.four = 5
                self.five = 5
        else:
            for _ in range(20):
                self.one = random.randint(2, 4)
                self.two = random.randint(2, 4)
                self.three = random.randint(2, 4)
                self.four = random.randint(2, 4)
                self.five = random.randint(2, 4)


    def average(self):
        for _ in range(20):
            self.scores = (self.one + self.two + self.three + self.four + self.five) / 5
        return self.scores

    def rating(self, scores):
        for i in range(len(scores)):
            for j in range(len(scores) - 1):
                if scores[j].average() < scores[j + 1].average():
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores


name_of_groups = ['БФЗ-24-1', 'БМТМ-24-1','БЭН-24-1']

list = [Exams(name_of_group) for name_of_group in name_of_groups]

exams = Exams("")
success = exams.rating(list)


print('Рейтинг групп:')
for group in list:
    print(f"{group.name_of_group}: Средний балл: {group.average():}")
