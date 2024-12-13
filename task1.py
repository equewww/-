'''В заданной матрице элементы каждой строки расположить в порядке возрастания. Упорядочение элементов строки оформить в виде метода.'''

import random

# Функция для упорядочения строк матрицы:
def sort_m(m):
    for i in m:
        i.sort()
    return m

k = input('Введите количество строк: ')
i = input('Введите количество столбцов: ')

# Рандомно создаем матрицу:
m  = [[random.randint(-100, 100) for _ in range(int(i))] for _ in range(int(k))]
print('Матрица:')
for i in m:
    print(i)

# Используем функцию:
sorted_m = sort_m(m)

print('Упорядоченная матрица:')
for i in sorted_m:
    print(i)
