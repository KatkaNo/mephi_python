i = 0
j = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a > 0:
        i += 1
    if a < 0:
        j += 1
print('Кол-во положительных чисел: ',i)
print('Кол-во отрицательных чисел: ',j)