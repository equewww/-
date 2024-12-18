''' На основании результатов соревнований по прыжкам в длину (фамилии и результаты трех попыток)
составить итоговый протокол соревнований, считая, что в зачет идет лучший результат.'''
import random

class Jump:
    def __init__(self, surname):
        self.surname = surname
        self.first = round(random.uniform(0, 4), 2)
        self.second = round(random.uniform(0, 4), 2)
        self.third = round(random.uniform(0, 4), 2)

    # Функция для определения лучшего прыжка
    def best(self):
        if self.first <= self.second and self.third <= self.second:
            return self.second
        elif self.first >= self.second and self.third <= self.first:
            return self.first
        elif self.first <= self.third and self.third >= self.second:
            return self.third

surnames = ['Исаев Д. Е.      ', 'Спиридонова В. Д.', 'Гончарова К. И.  ', 'Макарова А. А.   ',
            'Васильев М. А.   ', 'Сафонов М. Т.    ', 'Мещеряков И. М.  ', 'Майоров Т. А.    ']

# Формируем список спортсменов
athletes = [Jump(surname) for surname in surnames]

print('Протокол соревнований:')
for athlete in athletes:
    print(athlete.surname, ': Лучший прыжок: ', athlete.best(), ': ( Первый: ', athlete.first, 'Второй: ', athlete.second, 'Третий: ', athlete.third, ')')
