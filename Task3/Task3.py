'''
Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
Формат: Объясняет преподаватель

Задача: предложить улучшения кода для уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
3 Исправленные задачи на Отлично!

'''
from functools import reduce

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Первое рещение
# n = int(input('Введите натуральное число:'))
# f = 1
# list = []
# for i in range(n):
#     f = f * (i + 1)
#     list.append(f)
# print(list)

# Улучшенное решение
from itertools import accumulate

n = int(input('Введите натуральное число:'))
lst = list(range(1, n + 1))
a = map(lambda x: max(x,1), lst)
print(*accumulate(a, lambda x, y: x * y))
