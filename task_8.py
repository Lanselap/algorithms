# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

M = 5
N = 5
a = []
for i in range(1, N):
    b = []
    s = 0
    print(f'{i}-я строка: ')
    for j in range(M - 1):
        n = int(input('Введите целое число: '))
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)
