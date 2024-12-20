#  Сформировать одномерный массив из количеств отрицательных элементов столбцов матрицы A размером 4 х 3.

import random
m  = [[random.randint(-100, 100) for _ in range(3)] for _ in range(4)]
print('Матрица А:')
for i in m:
    print(i)

negative_counts = [0] * 3

for i in range(4):
    for j in range(3):
        if m[i][j] < 0:
            negative_counts[j] += 1

print("Количество отрицательных элементов в каждом столбце:", negative_counts)