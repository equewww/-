"""В матрице В размером 6 х 6 поменять местами максимальные
элементы 1-й и 2-й строк, 3-й и 4-й, 5-й и 6-й."""

'''
import random
m  = [[random.randint(1, 100) for _ in range(6)] for _ in range(6)]
print('Матрица:')
for i in m:
    print(i)
'''

m= []
for i in range(6):
    s = input('Введите строку матрицы ').split()
    m.append(s)

max1 = 0
max2 = 0
i1=0
i2=0
for i in range(0, 6, 2):
    for k in range(6):
        if int(m[i][k]) > int(max1):
            max1 =m[i][k]
            i1 = k
    for n in range(6):
        if int(m[i+1][n]) > int(max2):
            max2 = m[i+1][n]
            i2=n
    m[i][i1], m[i+1][i2] = m[i+1][i2], m[i][i1]
    i1=0
    i2=0
    max1 = 0
    max2=0
print('Матрица:')
for i in m:
    print(i)