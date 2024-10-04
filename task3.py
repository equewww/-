"""Из массива размером 12 удалить все отрицательные элементы"""
m= []
for i in range(12):
    m.append(int(input('Введите элемент массива: ')))
mi = min(m)
while mi < 0:
    m.remove(mi)
    mi = min(m)
print('Массив:',m)