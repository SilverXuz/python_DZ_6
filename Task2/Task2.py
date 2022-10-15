'''
Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
Формат: Объясняет преподаватель

Задача: предложить улучшения кода для уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
3 Исправленные задачи на Отлично!

'''
# - A (3,6); B (2,1) -> 5,09
# Первое решение
# print('Введите координату X1: ')
# x1 = int(input())
# print('Введите координату Y1: ')
# y1 = int(input())

# print('Введите координату X2: ')
# x2 = int(input())
# print('Введите координату Y2: ')
# y2 = int(input())

# result = (((x2 - x1)**2) + ((y2-y1)**2)) ** 0.5
# print(f'{float(result):.3f}')

# Улучшенное решение
spisok = ['x1', 'y1', 'x2', 'y2']
x = [int(input(f'Введите координату {spisok[_]}: ')) for _ in range(len(spisok))]
xy = (((x[0] - x[2])**2) + ((x[1]-x[3])**2)) ** 0.5
print(f'{(xy):.3f}')
