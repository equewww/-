''' Лыжные гонки проводятся отдельно для двух групп участников. Результаты соревнований заданы в виде фамилий участников
и их результатов в каждой группе. Расположить результаты соревнований в каждой группе в порядке занятых мест.
Объединить результаты обеих групп с сохранением упорядоченности и вывести в виде таблицы с заголовком. '''

import random
class Skiing:
    def __init__(self, surname):
        self.surname = surname
        self.result = random.randint(120, 150)


    def bubble_sort(members):
        n = len(members)
        for i in range(n):
            for j in range(0, n - i - 1):
                if members[j].result > members[j + 1].result:
                    members[j], members[j + 1] = members[j + 1], members[j]

surnames_group_1 = ['Исаев Д. Е.      ', 'Спиридонова В. Д.', 'Гончарова К. И.  ', 'Майоров Т. А.    ']
surnames_group_2 = ['Макарова А. А.   ', 'Васильев М. А.   ', 'Сафонов М. Т.    ', 'Мещеряков И. М.  ']

members_group_1 = [Skiing(surname) for surname in surnames_group_1]
members_group_2 = [Skiing(surname) for surname in surnames_group_2]

Skiing.bubble_sort(members_group_1)
Skiing.bubble_sort(members_group_2)

print('')
print('  Результаты соревнований 1 группы:')
print("Место         |","Фамилия         |","Время")
print('-' * 45)
n=1
for member in members_group_1:
    print(n,'     |',member.surname,'     |',member.result)
    n+=1

print('')
print('  Результаты соревнований 2 группы:')
print("Место         |","Фамилия         |","Время")
print('-' * 45)
n=1
for member in members_group_2:
    print(n,'     |',member.surname,'     |',member.result)
    n+=1