"""В заданной матрице удалить все строки, содержащие нулевые элементы."""

'''
import random
k = input('Введите количество строк: ')
i = input('Введите количество столбцов: ')
m  = [[random.randint(-100, 100) for _ in range(int(i))] for _ in range(int(k))]
print('Матрица:')
for i in m:
    print(i)
'''

m= []
n = input('Введите размер матрицы через пробел: ').split()
for i in range(int(n[0])):
    s = []
    for k in range(int(n[1])):
        s.append(int(input('Введите элемент строки в матрице: ')))
    m.append(s)
    print('Следующая строка:')

print('Матрица: ')
for i in m:
    print(i)
m = [i for i in m if 0 not in i]
print('Матрица:')
for i in m:
    print(i)