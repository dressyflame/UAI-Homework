# -*- coding: utf-8 -*-
"""
(МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
"""

print('Введите элементы 1-го списка: ', end = '')
seq1 = [int(i) for i in input().split(',')]

dic_seq1 = dict()

for i in range(len(seq1)):
    if seq1[i] in dic_seq1.keys():
        dic_seq1[seq1[i]] += 1
    else:
        dic_seq1[seq1[i]] = 1

print('Введите элементы 2-го списка: ', end = '')
seq2 = set([int(i) for i in input().split(',')])

for i in seq2:
    if i in dic_seq1.keys():
        dic_seq1.pop(i)

seq1 = []
for i in dic_seq1.keys():
    for j in range(dic_seq1[i]):
        seq1.append(i)
    

print(*sorted(list(seq1)), sep = ', ')