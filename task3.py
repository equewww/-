'''Заданный массив преобразовать таким образом, чтобы все его
элементы принадлежали отрезку [-1, 1). Предусмотреть возможность
обратного преобразования.'''

n = int(input('Введите количество элементов массива: '))
if n == 0:
    print('Ошибка')
else:
    m = []
    for x in range(int(n)):
        m.append(int(input('Введите элемент массива: ')))

min = m[0]
max = m[0]

for x in m:
    if x < min:
        min = x
    if x > max:
        max = x

m1 = []
for x in m:
    a = 2 * (x - min) / (max - min) - 1
    m1.append(a)

print("Преобразованный массив:", m1)

m2 = []
for x in m1:
    b = ((x + 1) / 2) * (max - min) + min
    m2.append(b)

print("Обратное преобразование:", m2)