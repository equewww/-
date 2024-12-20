'''Объединить массивы А размером 7 и B размером 8, предварительно удалив максимальные элементы этих массивов.
Результат получить в массиве А. Удаление элемента массива с заданным индексом осуществить в методе.'''

import random

def remove_max_element(m):
    max_value = max(m)
    m.remove(max_value)
    return m

A  = [random.randint(-100, 100) for _ in range(7)]
print('Массив А:')
print(A)

B  = [random.randint(-100, 100) for _ in range(8)]
print('Массив В:')
print(B)

new_A = remove_max_element(A)
new_B = remove_max_element(B)

A.extend(B)

print("")
print("Результат:", A)