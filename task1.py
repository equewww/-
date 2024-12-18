'''Группа учащихся подготовительного отделения сдает выпускные экзамены
по трем предметам(математика, физика, русский язык). Учащийся, получивший «2», сразу отчисляется.
Вывести список учащихся, успешно сдавших экзамены, в порядке убывания полученного ими среднего балла по результатам трех экзаменов.'''
import random

class Exams:
    def __init__(self, surname):
        self.surname = surname
        self.math = random.randint(2, 5)
        self.physics = random.randint(2, 5)
        self.russian = random.randint(2, 5)

    # Функция для определения сдавших экзамены студентов и вычисления средного балла
    def average(self):
        if self.math == 2 or self.physics == 2 or self.russian == 2:
            return None
        return (self.math + self.physics + self.russian) / 3

    # Сортируем студентов в порядке убывания среднего балла
    def filter(self, students):
        passed = [student for student in students if student.average() is not None]
        for i in range(len(passed)):
            for j in range(len(passed) - 1):
                if passed[j].average() < passed[j + 1].average():
                    passed[j], passed[j + 1] = passed[j + 1], passed[j]
        return passed

surnames = ['Исаев Д. Е.      ', 'Спиридонова В. Д.', 'Гончарова К. И.  ', 'Макарова А. А.   ',
            'Васильев М. А.   ', 'Сафонов М. Т.    ', 'Мещеряков И. М.  ', 'Майоров Т. А.    ',
            'Николаева Е. К.  ', 'Павлов П. М.     ', 'Михайлова М. Е.  ', 'Бочаров М. В.    ',
            'Сидоров Е. Ф.    ', 'Ефимова М. А.    ', 'Павловская А. Е. ', 'Федорова Л. А.   ',
            'Дмитриев М. А.   ', 'Киреев Д. А.     ', 'Елисеева М. Т.   ', 'Беляков И. М.    ']

# Формируем список студентов
students = [Exams(surname) for surname in surnames]

exams = Exams("")

# Формируем список студентов, успешно сдавших экзамены, в порядке убывания
success = exams.filter(students)

print('Успешно сдали:')
for student in success:
    print(student.surname, ': Средний балл: ',round(student.average(), 1),': ( Математика: ', student.math, 'Физика: ',student.physics, 'Русский:',student.russian, ')')
