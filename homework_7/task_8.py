number = int(input('Введите натуральное число: '))
s = 1
x = 1
for n in range(1, number + 1):
    x = ((-1) ** n) / (2 ** n)
    s += x
print('Член ряда ', x,'сумма ряда ', s)
