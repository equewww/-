'''В двух заданных матрицах найти максимальные элементы и поменять их местами. Поиск максимального элемента матрицы оформить в виде метода.'''

import random

# Создаем функцию для поиска максимального элемента в матрице
def find_max(m):
    max_value = m[0][0] # Значение максимального элемента
    max_position = (0, 0) # Позиция максимального элемента
    
    # Поиск:
    for i in range(len(m)):
        for k in range(len(m[i])):
            if m[i][k] > max_value:
                max_value = m[i][k]
                max_position = (i, k)

    return max_value, max_position

# Создаем функция для перемещения элементов
def swap(m1, m2):
    max1_value, max1_position = find_max(m1) # Ищем максимальный элемент в первой матрице
    max2_value, max2_position = find_max(m2) # Ищем максимальный элемент во второй матрице
    m1[max1_position[0]][max1_position[1]] = max2_value # Присваиваем максимальному элементу первой матрицы значение второго максимального
    m2[max2_position[0]][max2_position[1]] = max1_value # Присваиваем максимальному элементу второй матрицы значение первого максимального 
    
# Создаем матрицы:
k1 = input('Введите количество строк 1 матрицы: ')
i1 = input('Введите количество столбцов 1 матрицы: ')
m1  = [[random.randint(-100, 100) for _ in range(int(i1))] for _ in range(int(k1))]

k2 = input('Введите количество строк 2 матрицы: ')
i2 = input('Введите количество столбцов 2 матрицы: ')
m2  = [[random.randint(-100, 100) for _ in range(int(i2))] for _ in range(int(k2))]
print('1 матрица:')
for i1 in m1:
    print(i1)
print('2 матрица:')
for i2 in m2:
    print(i2)
    
# Используем функцию замены максимальных элементов
swap(m1, m2)
print("1 матрица после замены:")
for i1 in m1:
    print(i1)
print("2 матрица после замены:")
for i2 in m2:
    print(i2)
